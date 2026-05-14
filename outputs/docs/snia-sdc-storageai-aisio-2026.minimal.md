# SNIA SDC: StorageAI 2026 - AiSIO: Orchestrating Storage I/O Across CPUs and Accelerators

channel: SNIAVideo
uploaded: 2026-05-12
duration: 29m 34s
url: https://www.youtube.com/watch?v=AJe22Nah5KA
transcript_source: manual (en)

## Overview
A Samsung researcher presents AiSIO (Accelerator-integrated Storage I/O, also called ACIO), an open-source project for orchestrating NVMe storage I/O across CPUs and GPU accelerators, at the SNIA Storage Developer Conference StorageAI 2026. The talk covers three software-layer challenges that limit accelerator I/O, three supported I/O modes, the new architecture replacing an earlier prototype, the open-source component ecosystem, and benchmark results comparing CPU baseline performance with peer-to-peer GPU-targeted I/O across multiple software layers.

## Chapter summaries
### Introduction and Problem Statement (00:00:05–00:03:43)
- The project is called Accelerator Integrated Storage IO (AiSIO), presented by a Samsung researcher. [00:09]
- Three challenges are identified: (1) software layer overhead at applications, libraries, language runtimes, user/kernel boundary, and OS storage stack; (2) unnecessary data copies bouncing through host DRAM before reaching the accelerator; (3) the single physical function limitation where one device exposes one PCIe physical function, allowing only one driver association. [00:22]
- Three I/O modes are targeted: CPU initiated (data to host memory), CPU initiated peer-to-peer (CPU drives, data to accelerator memory), and device initiated peer-to-peer (accelerator initiates, data to its own memory). [02:15]
- The stated design philosophy is interoperability over replacement: extend the existing software stack without trading off existing abstractions or performance. [02:47]
- The project targets upstream Linux kernel and open-source projects. [03:03]
- The stated vision is to have accelerators as first-class citizens in the storage stack. [03:14]

### Related Work and Initial Prototype (00:03:43–00:08:22)
- Existing solutions cited: Nvidia GDS (GPU Direct Storage), BAM (Big Accelerator Memory research project), Nvidia Scattera, AMD ROCk XIO, and ACIO. [03:43]
- Benchmarking of Nvidia GDS for small I/O showed that a single thread at small IO sizes could not saturate even a single NVMe device. [04:25]
- The initial prototype was based on BAM and libenvm prior work; the team reproduced device-initiated IO from those projects. [05:11]
- The prototype enabled coexistence of multiple control paths on a single drive using multiple physical functions (SIOV), with a kernel stack path and an ACIO prototype path running simultaneously. [05:36]
- A file extend cache was built so the GPU can directly load LBAs into its memory without repeated filesystem lookups. [06:19]
- Prototype comparison: ACIO prototype matched BAM for block IO workloads; GDS showed degraded performance especially at 96 threads. [07:00]
- File throughput comparison across small files and larger datasets showed benefits for smaller file workloads. [07:31]
- Challenges with the prototype included codebase compliance with the open-source stack, upstream feasibility, and file extent lookup reliability. [07:57]

### New AiSIO Architecture (00:08:22–00:11:46)
- The new architecture replaces libvm, custom kernel patches, and exclusive device ownership. [08:22]
- Main control-plane component is HOMIE, the Host Orchestrated Multipath IO Daemon, which brings up the multiple IO paths on the host. [08:35]
- UDMA buff import provides access to physical addresses on GPU memory. [08:49]
- The Extend Access Library caches file extent information inside HOMIE so user-space processes can retrieve it on demand. [09:42]
- A key change from the prototype is replacing raw XFS on-disk format decoding with the kernel's F_MAP_AP interface to retrieve file extent locations. [10:03]
- User-space processes access HOMIE via UIO PCI generic and VFIO PCI kernel interfaces, with a small ioctl tapping into the DMA buff and UDMA buff interfaces. [10:29]
- When a storage device supports SIOV or multiple physical functions, hardware-assisted multi-driver binding is used; for single-function devices, the Ublock infrastructure in the Linux kernel enables a software-based user-space control plane. [11:00]

### Open Source Components (00:11:46–00:16:19)
- AiSIO is composed of multiple open-source projects; existing ones shown in blue and new or extended ones shown in orange on the component diagram. [12:01]
- XNME: user-space library encapsulating different IO interfaces across platforms, extended with AiSIO primitives so that anywhere XNME is integrated the new IO paths can be used. [12:14]
- XME Perf: benchmarking tool with minimal overhead for executing CPU-initiated and device-initiated IO patterns. [12:37]
- UPC: module providing MMIO primitives for ringing the doorbell on a PCIe device, usable from CPU or accelerator. [13:02]
- A small DMA buff infrastructure tap module is not yet upstream and is awaiting Linux kernel community feedback. [13:31]
- Extend Access Library evolved through three backends: raw XFS on-disk decode, F_MAP_AP, and a planned F_MAP_AP plus EBPF traces to capture file change notifications. [13:56]
- Around 14:34, an audience member identified as Christoph Hellwig interrupted to object to the approach, characterizing it as dangerous. [14:34]
- Field Path: file-level benchmarking tool comparing POSIX, GDS CUFILE, and AiSIO interfaces. [15:02]
- CHO: provisioning tool analogous to Ansible for reproducible deployment of the AiSIO stack. [15:49]
- A white paper and SDK are publicly available for the project. [16:14]

### Benchmark Results (00:16:19–00:25:20)
- Test system: 16 NVMe drives in a Dell server hosted at Samsung Memory Research Center. [16:40]
- Drives run in unallocated mode (NVME LBA format) to measure CPU processing cost without media latency; per-drive capacity at this mode is 3.8 million IOPS. [16:51]
- Baseline with SPDK BDEV Perf: 62 million IOPS with eight CPU cores saturating all 16 devices. [17:35]
- IOPS scale linearly from one to two cores at approximately 7.7 million IOPS per core; NUMA effects produce some variation. [17:46]
- Application-layer comparison: BDEV Perf yields 6.3 million IOPS with one hardware thread, 7.4 million with two hardware threads, 16 million with three hardware threads on two CPU cores. [18:42]
- Replacing BDEV Perf with NVME Perf (same driver, BDEV layer removed) shows a dramatic improvement at the application level. [19:01]
- XME Perf (using the same SPDK NVME driver via XNME) further increases throughput to 32 million IOPS with three hardware threads. [19:21]
- Tweaking the driver layer with UPCE tooling: approximately 40 million IOPS on a single hardware thread; approximately 50 million IOPS on a single CPU with two hardware threads; at this point the system is bottlenecked by the number of NVMe devices, not software. [19:52]
- Overall CPU efficiency result: from 8 cores for 62 million IOPS reduced to 1.5 cores equivalent after optimization. [20:54]
- CPU initiated peer-to-peer (data landing on GPU): same IOPS ceiling as the host-memory baseline, with no additional CPU cost for DMA targeting the GPU. [21:28]
- Device initiated peer-to-peer: demonstrated as functional, reaches the same IOPS ceiling; GPU resource cost for this mode not reported in the slides. [22:17]
- Peer-to-peer bandwidth: three NVMe drives saturate the PCIe Gen 5 GPU link at 4K IO size; adding a fourth drive yields minimal gain. [24:02]
- At 4K IO size, a single CPU can saturate 8 GPUs in bandwidth terms. [25:04]

### Conclusion and Q&A (00:25:20–00:29:31)
- The stated vision is accelerators integrated into the storage stack with multiple IO modes while file systems, files, and OS still exist; all components are open source and either already upstream or targeting upstream. [25:36]
- New device-initiated experiments with additional results are described as available. [26:06]
- Source code and white paper are publicly available. [26:13]
- During Q&A, Christoph Hellwig delivered a fuller objection characterizing the F_MAP_AP-based approach as a debugging tool with file-system-specific content that poses corruption risk due to concurrent activity; he stated he had raised this concern with the team and its management two years earlier and recommended expanding PFS block layout with relocation mechanisms for defending clients. [26:35]
- The main speaker responded that the team also sees benefits in PNF and flex files as a management and abstraction layer, and that F_MAP_AP is not used exclusively. [27:14]
- In the benchmark experiments, files were pre-allocated and fixed size. [27:54]
- The data-loader workload used an image dataset (including a TikTok dataset) and large 8-gigabyte files, accessed randomly from the GPU; the workload design was inspired by the Nvidia DALI framework. [28:19]

## Full transcript
[00:05] session and um I'm pretty excited to
[00:08] talk about one of the many projects we
[00:09] do at Samsung. It's called accelerator
[00:12] integrated storage IO and this session
[00:15] in particular is focusing on the how to
[00:17] orchestrate storage IO across CPUs and
[00:20] accelerators.
[00:22] Now the and specifically focusing on
[00:25] these three challenges that we've uh
[00:27] seen where the main focus is actually up
[00:29] here on the software layer. So that's
[00:33] applications, libraries, even language
[00:35] runtimes, the boundaries between user
[00:37] and kernel space and the cost on every
[00:39] IO, the OS storage stack, how that comes
[00:42] in and and puts um a bit of latency on
[00:45] your IO's and even at the layer where we
[00:48] see different drivers
[00:50] are sort of paying different costs per
[00:53] IO based on the general generality that
[00:55] they need to support and the
[00:57] abstractions and also this other thing
[00:59] of unnecessary data copies And I should
[01:02] maybe have said not necessarily
[01:03] unnecessary. They're there for a reason,
[01:06] but definitely unwanted memory copies of
[01:09] data bouncing through host DAM before
[01:11] reaching your accelerator. And then the
[01:13] third thing I think this might have been
[01:15] familiar to most of you but the last
[01:16] thing might be not might not be which is
[01:19] basically this thing at the system
[01:21] software level where a single device
[01:24] usually exposed as PCE as one uh
[01:27] physical function you can only associate
[01:29] a single driver to manage that in your
[01:31] operating system. So these things
[01:34] provide this sort of a funnel uh
[01:36] reduction of what's uh or how we can
[01:39] make storage available to your
[01:40] accelerators and most of it is due to
[01:43] the way that stuff has been managed
[01:45] today for CPUs and the challenges just
[01:49] get even bigger when it comes to then
[01:50] feeding data from your NVME storage into
[01:53] your accelerator.
[01:54] And that brings us to the accelerator
[01:56] integrated storage IO project. It
[01:58] started out as being accelerator
[02:00] initiated, a big focus on that. But we
[02:03] quickly came to realize that making sure
[02:06] that we have a unified way of talking
[02:08] about data movement and moving data
[02:10] around. We can't just focus on the
[02:12] device initiated part. So we want to be
[02:15] able to support three IO modes. One is
[02:17] CPU initiated. Data ends up CPU drives
[02:20] it. Data ends up in host memory. CPU
[02:23] initiated peer-to-peer. So the CPU is
[02:25] still in the driver seat, but the data
[02:27] ends up in an accelerator memory. And
[02:29] then there's device initiated
[02:30] peer-to-peer where the data accelerator
[02:33] initiates the the IO data ends up in its
[02:36] own memory. And a big focus on how we
[02:39] can preserve support for files, file
[02:42] system and OS control while enabling
[02:45] these different IO modes. So a big focus
[02:47] on interoperability over replacement. So
[02:50] basically we want to extend the existing
[02:52] software stack and we want to do so in
[02:55] ways where we're not trading off the
[02:57] utilities of having existing
[02:59] abstractions and we don't want to trade
[03:01] off performance either. And our focus is
[03:03] in doing this in an open-source way
[03:05] where we're either already now um
[03:09] targeting upstream or actually in
[03:11] upstream as open source projects. So
[03:14] that's the vision. We want to be able to
[03:16] have accelerators as uh uh first class
[03:20] citizens in the um in the storage stack.
[03:24] And for this presentation, I'll be going
[03:27] through the first two things that we'll
[03:29] cover uh rather quickly. It's about
[03:31] where we started out with the P last
[03:33] year. Uh what the challenges were with
[03:35] that and then what we're building
[03:37] instead, what you can do with it, what
[03:39] the benefits are, and where we're going
[03:40] to take this from here.
[03:43] So as you are probably very familiar
[03:45] with you have Nvidia GDS out there as
[03:47] one way of instrument instrumenting data
[03:49] movement getting stuff from NVMe into
[03:52] your accelerators. There's a research
[03:54] project called BAM that's a big
[03:56] accelerator memory project. It's one of
[03:59] the things that really started focusing
[04:00] on device initiated IO. Then you have
[04:03] Nvidia scattera project. Um and very
[04:06] recently I saw that AMD announced
[04:08] something they called a rock or rock XIO
[04:11] which is also a device initiated IO from
[04:13] the GPU and then there's ACO which this
[04:17] talk is all about. Now we wanted out
[04:20] initially to figure out what is really
[04:22] the problem and this is what we saw. So
[04:25] benchmarking Nvidia GDS here especially
[04:28] for small IO and as you saw in the
[04:30] previous talk small IO is very relevant
[04:33] and basically here you have bandwidth on
[04:35] the y-axis and on the x-axis you have
[04:38] the the um IO size as you scale IO size
[04:42] you amatize the cost of doing IO so that
[04:44] means you get more bandwidth as you
[04:46] increase your IO size another thing you
[04:48] can do is then scale up the amount of
[04:50] workers doing work that's what you see
[04:52] on the other graph here so here we go
[04:54] from one CPU thread up to 96. So it
[04:58] doesn't look great. So here a single
[05:00] thread small IO we cannot saturate even
[05:04] a single NVME device using this. So
[05:06] that's what we set out to figure out
[05:08] what can we do about that and based on
[05:11] the the prior work of BAM where they
[05:13] showed what they could be able to do
[05:14] with device initiated and the work of
[05:16] libenvm we reproduced what they have
[05:19] been doing and wanted to extend that and
[05:22] figure out could we also have file
[05:24] system support and the way we did that
[05:27] was to look at two things one is the
[05:30] coexistence of multiple um like control
[05:33] paths or associations with a single
[05:36] drive. So looking at a single drive that
[05:38] usually just exposes one physical
[05:40] function that you bind a driver to and
[05:43] that means that over here you're either
[05:45] talking to a kernel stack or some other
[05:48] user space driven stack to talk to your
[05:50] device. But having physical multiple
[05:53] functions on your device, you can start
[05:55] binding multiple drivers and by doing so
[05:58] uh having these multiple tenants on one
[06:01] drive.
[06:02] And with that we showed how we can then
[06:04] have the entire kernel space running
[06:07] with your traditional IO and kernel
[06:09] manage mode along with this stack over
[06:12] here that we call the acco prototype.
[06:14] And in that thing we sort of have a
[06:16] cache for all of the file operations. So
[06:19] one essential thing of loading data from
[06:21] storage into your GPU is that you need
[06:24] to know where your files are. So and
[06:27] that's the that's the entire task of the
[06:29] storage operating system of the file
[06:30] system. It knows the mapping from a file
[06:33] name down to the LBAS where the data is
[06:35] actually stored. So you need to extract
[06:37] that. That portion is uh time consuming.
[06:41] So you need a way to make that faster
[06:43] and we do by that by caching those um
[06:46] those address translations such that the
[06:48] GPU can directly go and load those LBAS
[06:51] into its memory. So that was the first
[06:54] uh PC we did and we uh the numbers that
[06:57] came out of it was a comparison here
[07:00] between GDS and BAM and here we're just
[07:03] doing like sort of a a synthetic block
[07:06] IO and we what we wanted to see that we
[07:09] could match when doing a workload that
[07:11] is entirely block IO we match what BAM
[07:14] did and we could do uh and you see the
[07:17] trouble here with with GDS down here uh
[07:20] and this is 96 threads and over here you
[07:23] have um uh run thread. So that sort of
[07:26] paints the picture of the the trouble of
[07:28] those existing solutions.
[07:31] Now what we then enabled was the file
[07:33] support. So here we have uh file
[07:35] throughput compared on three different
[07:37] workloads. One is small files and then
[07:39] larger and larger data sets. So as of
[07:42] course as larger the files are the lower
[07:45] the the benefit is but it's pretty clear
[07:47] that it is possible to reduce some of
[07:49] that bottlenecks that were related to uh
[07:51] what we saw with the prior work and we
[07:54] can get those things to cooperate.
[07:57] However, there are a bunch of challenges
[07:59] we needed to address with that um PC
[08:01] stack and it's a lot about the the
[08:04] codebase is used and how they
[08:05] interoperated with the open-source stack
[08:08] and we wanted something that could move
[08:10] forward in a way that would be compliant
[08:12] and something we could upstream. We also
[08:14] had challenges at the stuff that we
[08:16] added with regards to file extends and
[08:18] looking up those things. So, we wanted
[08:20] to address that as well.
[08:22] So jumping into it, what we came from
[08:25] was this infrastructure where we use
[08:26] libvm and these custom kernel patches
[08:29] and that uh exclusive uh device
[08:32] ownership. So the main components now is
[08:35] this thing called homie the host
[08:37] orchestrated multiath IO demon. That's
[08:41] the control plane that sits at the host.
[08:43] It brings up everything and make sure
[08:45] that you have the multiple IO paths
[08:47] available. And then a small component
[08:49] here with UDMA buff import that lets us
[08:53] get access to the to um the the physical
[08:56] addresses on the GPU memory. And then
[08:59] expanding this with uh all three IO
[09:02] modes. So that brings us to here we're
[09:05] just recapping what we had before um the
[09:08] interfaces we used that interface
[09:10] directly specifically with CUDA and the
[09:13] NVIDIA kernel driver and this libm
[09:16] kernel module. and we had bund like
[09:18] bundle everything into a single process.
[09:20] Having a single process has of course a
[09:22] lot of challenges since that's not
[09:24] really the use case out there. You have
[09:26] a ton of different processes that needs
[09:28] to access files and need to make sure
[09:30] that data are actually running into your
[09:33] GPU. So the first thing we do is split
[09:35] that up and that's the the homie demon.
[09:38] That's the control plane running on your
[09:40] hosts. It does through this library
[09:42] called the extend access library. That's
[09:44] where it caches uh all of that extend
[09:47] info. And a major thing that changed
[09:49] here is that previously we went through
[09:52] and directly decoded the XFS on disk
[09:54] format. That's a bit brittle to do that
[09:57] and doesn't really scale well since we
[09:59] had to do this for every file system out
[10:01] there. Uh fortunately, the kernel has a
[10:03] very neat feature of F mapap where we
[10:05] can just ask the kernel where are your
[10:08] where are your things lying. So that was
[10:11] one thing we we could then do and then
[10:13] have that uh efficiently cached inside
[10:16] of our homie demon. Uh and then for
[10:18] other user space processes that then
[10:20] need to access this they can then do
[10:22] that now and talk to the demon to get
[10:25] the state of the user space drivers up
[10:27] and running. And the thing they need to
[10:29] talk with the kernel to do this are the
[10:31] existing UIO PCI generic and VFIO PCI.
[10:35] And then we have a small tiny layer here
[10:37] with an ioctal that taps into the DMA
[10:40] buff interface and UDMA buff interface.
[10:43] And with that we can talk with the
[10:46] driver for the accelerator uh that
[10:48] supports the DMA buff export interface.
[10:51] Get that so we can get the addresses
[10:53] where we need to form our DMA uh to be
[10:56] performed directly to the um to the
[10:58] accelerator.
[11:00] Then this works well once your storage
[11:03] device supports SIOV or another way of
[11:06] having multiple functions on your
[11:07] storage device. But we want to be able
[11:09] to deploy this even further. And that's
[11:12] where we can make use of Ublock. So the
[11:15] Ublock infrastructure in the Linux
[11:16] kernel gives us a way to implement the
[11:19] block device driver in a way where we
[11:22] then tap into that user space control
[11:24] plane on the kernel and then down again
[11:27] for the setup of all of the drivers
[11:29] that's running inside of a in user
[11:32] space. And by doing this we can sort of
[11:34] have either go the hardware assisted
[11:36] route or we can do something that is uh
[11:39] running based on on software when the
[11:41] device only supports a single uh
[11:43] physical function.
[11:46] Now just a brief overview with the new
[11:50] ACO open source implementation. It
[11:53] consists of a bunch of o open source
[11:55] product uh projects uh different
[11:57] components you might say. And what's
[11:59] showing here is just the names of these
[12:01] things and the blue ones are stuff that
[12:03] already exist. These purple or sorry
[12:06] these orange ones are um stuff we either
[12:10] had to add or extend the existing
[12:12] versions of.
[12:14] And uh I'll just be going briefly
[12:16] through what these different projects
[12:17] are. So Xenme is a userbased library
[12:20] that encapsulates a bunch of different
[12:22] IO interfaces uh on different platforms
[12:26] and it has been extended with these acco
[12:28] primitives such that we can use uh
[12:31] anywhere XME is integrated we can then
[12:33] make use of these new IO paths. Uh XME
[12:37] Perf was a tool we needed and I'll come
[12:39] back later why we needed to do this.
[12:41] that allows us to uh with minimal
[12:44] overhead do some very simple IO uh
[12:47] patterns and you can see it running over
[12:50] here where it's executing IO either
[12:52] through the CPU initiated path or the
[12:55] device initiated path um and UPC is a
[12:59] small module that uh gives us the
[13:02] primitives to do MMIO in a convenient
[13:05] way both on the CPU and on an
[13:08] accelerator and we sort of needed a
[13:10] place where we could have an abstract
[13:11] ction over these small primitives. So
[13:13] that's the thing that allows us to ring
[13:15] the doorbell on a PCE device and we want
[13:18] to encapsulate that in a way such that
[13:20] it's easier to build drivers on top
[13:22] whether that's in user space on the host
[13:24] or on an accelerator inside of the the
[13:27] the kernel language for that
[13:29] accelerator.
[13:31] Um and then uh the main thing uh that
[13:35] sort of enables us to tap into the DMA
[13:38] buff infrastructure of the Linux kernel
[13:40] is this small uh thing here. It's not
[13:42] upstream. It's something where we want
[13:44] to engage with the Linux kernel
[13:45] community today. Um but uh it is we've
[13:49] made it openly available so we could get
[13:51] some feedback on how we can proceed with
[13:53] this. Uh there's the extend access
[13:56] library. That's the component that sort
[13:58] of tries to abstract how we're getting
[14:00] the extend information and initially we
[14:03] did the raw decode which was not
[14:05] optimal. uh we then did the F mapap back
[14:07] end and now we're looking at doing F
[14:09] mapap plus EBPF traces such that we can
[14:12] capture not just so basically when when
[14:15] we do F mapap we also need to know when
[14:17] data changes then we can use I notify
[14:20] but when I notify happens you have
[14:22] another issue of then requesting F mapap
[14:24] afterwards but we're looking into maybe
[14:27] being able to get um EPF running such
[14:30] that we can get the notification of
[14:32] these changes
[14:34] &gt;&gt; let's do that afterwards Kristoff there
[14:36] is a proper way to do it and I told for
[14:38] two years to multiple members in your
[14:40] team how to do it and it's really
[14:43] upsetting that you can keep publishing
[14:45] kind of dangerous
[14:48] don't do that
[14:49] &gt;&gt; that's great let's talk about that
[14:50] afterwards
[14:52] &gt;&gt; I mean why are you claiming it's a good
[14:54] idea when your team knows how freaking
[14:57] dangerous
[14:59] &gt;&gt; that's one opinion what we also have is
[15:02] you a benchmarking tool called uh Field
[15:05] path is all about doing benchmarking at
[15:07] the file level such that we compare can
[15:10] compare PEX as well as uh the GDS coup
[15:13] file interfaces as well as doing the
[15:15] same thing with um the acco
[15:17] infrastructure.
[15:19] So we also touched a bit on the diagram
[15:23] about how Homie fits into this. So I
[15:25] won't dive into the details of that.
[15:27] It's either the Ublock approach of the
[15:29] isolation and multiple functions for
[15:32] binding drivers or there going through
[15:34] Ublock. That's sort of the the two ways
[15:36] of doing that. Then there's the Ublock
[15:40] server. A bunch of these things are also
[15:42] done in a way such that it'll be easy to
[15:44] others to pick up the work and reproduce
[15:46] it. And then uh that's done with
[15:49] something called CHO. You can think of
[15:50] that as you know uh if you're familiar
[15:53] with antible and other provisioning
[15:54] tools it's a bit uh down that road and
[15:58] in general the ACIO is a project where
[16:00] we're trying to do stuff in a way
[16:02] that'll be reproducible. So we have
[16:04] claims here stuff we're showing
[16:06] benchmarks things we're doing uh you can
[16:09] reproduce them and see that uh yeah
[16:12] where those numbers came from. Uh we've
[16:14] put out a white paper and an SDK so you
[16:16] can also experiment with it. So now
[16:19] let's dive into these uh four
[16:20] experiments where using AIO. We'll be
[16:23] looking at um establishing a CPU
[16:26] initiated baseline. Actually for this
[16:28] thing we're looking at something that
[16:30] wasn't uh um ACIO but what people
[16:33] usually do and then these other
[16:35] experiments that I'll that I'll go
[16:37] through. Now first off we're looking at
[16:40] these 16 uh NVME drives in a system. And
[16:44] since we're only interested in seeing
[16:46] what the cost is of CPU processing or
[16:48] processing of IOPS in general, we're
[16:51] using these in an unallocated fashion.
[16:54] That's basically when you just run NVME
[16:56] LBA format. So the drive spends less
[16:59] time since it doesn't actually has to go
[17:01] to the media to fetch the data. It can
[17:03] return much sooner. And by doing that,
[17:05] we can get 3.8 millions from these
[17:07] drives. It's a Dell server and then it's
[17:11] been hosted in something called Samsung
[17:12] Memory Research Center. Um, and we're
[17:15] looking at we've been doing this
[17:17] parameter suite looking at CPU governor,
[17:19] turbo boost, things you enable and
[17:21] disable in your BIOS, things you tweak
[17:23] in the kernel, uh, QEP, call count, all
[17:25] of these things. And the sweet spot we
[17:28] end up with here, and what we're using
[17:29] here is SPDK and something called that
[17:32] benchmarking tool called BDEF Perf. And
[17:35] we hit the 62 million IOPS here with
[17:38] eight CPU cores. So that's 16 devices.
[17:41] Uh that gets saturated by using eight
[17:44] CPU cores.
[17:46] So that's right around 7.7 million IOPS
[17:50] per core. Uh there is some variation you
[17:53] saw in the plot that can be attributed
[17:54] to NUMA effects. And the one good thing
[17:57] about this is that it scales linear
[17:59] linearly one to two. Um, and there's
[18:02] something to be said about the different
[18:04] things you have to tweak to get these
[18:06] numbers,
[18:07] but
[18:09] we really wanted to figure out, can we
[18:11] do better? Like, uh, could we free up
[18:13] all of these calls? We're spending eight
[18:16] CPU calls. That's quite a lot. So, what
[18:18] can be done about that? And for that, we
[18:21] wanted to look both at the application
[18:23] layer and at the driver layer. So, SPDK
[18:26] provides BDEV perf. It also provides
[18:28] NVME perf. Another tool BFP perfs has
[18:31] the abstraction layer of a block layer.
[18:33] MME Perf does not. And then there's this
[18:35] other tool we did called XME Perf. So
[18:38] let's take a look at that. So BDF Perf
[18:42] here a single CPU a single hardware
[18:44] thread 6.3 million and then with two
[18:47] hardware threads 7.4 million and using
[18:50] three uh hardware threads on two CPU
[18:53] cores it gets 16 million. Um so that's
[18:56] pretty much what we saw before. now
[18:59] using NVME perf. So that's the exact
[19:01] same NVME driver, but now we have
[19:03] tweaked that BDEV perf the BDEV layer
[19:07] has now been cut off. So this is just a
[19:10] small tweak at the application level and
[19:12] you can see some quite dramatic effects
[19:13] from that. And now you also see why we
[19:16] then did XME Perf because we saw we can
[19:18] tweak some of these things even further.
[19:21] And with XMME Perf, it taps through XME
[19:24] using the same driver as SPDK. And we
[19:27] get again just a little bit more. So
[19:30] this is tweaking application layer logic
[19:32] for doing uh random read workloads. And
[19:36] these are basically the results. So you
[19:38] ultimately here with three hardware
[19:39] threads you get 32 million IOPS. So
[19:42] that's application layer tweaking. Then
[19:45] we wanted to see so this was the SPDK
[19:47] and ME driver. What if we tweak the
[19:48] driver itself using these UPCE tooling?
[19:52] Well, then we end up even further. So, a
[19:55] single hardware thread now can do around
[19:57] 40 million IOPS. And over here with
[20:01] single CPU core, two hardware threads,
[20:03] we get very close to 50 million IOPS uh
[20:06] just by tweaking um yeah the application
[20:09] layer and the driver layer. And at this
[20:11] point here we get bottleneck by that we
[20:14] simply cannot put any more devices into
[20:16] this system.
[20:23] got through the the takeaways from that
[20:25] is that um by tweaking the application
[20:28] and the driver layers you can get a lot
[20:30] more out of the this the storage stack.
[20:34] Uh then if um yeah that that's the main
[20:37] purpose like uh there's overhead that is
[20:40] incurred at every layer that affects
[20:42] latency and that ultimately affects how
[20:44] many IOPS you can push through your
[20:46] system. So by remov removing that yeah
[20:49] you get more efficient system
[20:51] utilization. Uh so in this case we went
[20:54] from these eight cores to re reach 62
[20:57] million down to 1.5
[21:00] and um that's all good but we really
[21:03] need our data to get into the
[21:04] accelerator and for that we need to do
[21:07] something else and what you saw before
[21:09] data landed in host memory we need that
[21:11] data to land on the GPU. So for that uh
[21:16] the acco uh system has CPU initiated IO
[21:20] with peer-to-peer data movement and then
[21:22] device initiated IO with the
[21:24] peer-to-peer data movement. And let's
[21:26] have a look at how that stuff is doing.
[21:28] So just remember this graph here data l
[21:31] lands in host uh memory. We needed to go
[21:34] to the to the GPU or accelerator without
[21:38] paying an additional cost. And that's
[21:41] what we see here. you're running the XME
[21:43] Perf tool using the peer-to-peer mode.
[21:46] And what you see then is the data just
[21:49] lands the exact same place. The cost of
[21:51] the CPU utilization is the same. So what
[21:55] we don't have in the slides here is
[21:56] showing what the added cost would be to
[21:58] do the data copy from host down to the
[22:01] down to the um accelerator. But that's
[22:04] sort of not the point here. The point is
[22:06] that the NVME drive doesn't really care
[22:09] that the DMA address is on your host
[22:11] memory or on your GPU. The cost of
[22:14] processing that IO is the same. And then
[22:17] when we add the mode where the IO is
[22:20] initiated on the device side, well, we
[22:23] land in the same place here. So, of
[22:26] course, for this number, there's a lot
[22:27] more to the story. We're not using CPU
[22:30] resources anymore. And here we're not
[22:32] talking about how many GPU resources we
[22:34] are processing for this. We basically
[22:37] just want to demonstrate that it's it's
[22:39] currently possible. It's very recent but
[22:41] it's in the infrastructure. Now and the
[22:44] reason why you see here that it's the
[22:46] same is that well it's unrelated to the
[22:48] use of CPU uh processing.
[22:52] That uh sort of brings us to yeah
[22:55] basically
[22:56] both of these patch paths reach reach
[22:59] the same ceiling that we had before. Now
[23:01] data just ends up on your on your GPU uh
[23:05] w without paying any any extra cost for
[23:08] doing that.
[23:11] Uh then we have peer-to-peer bandwidth.
[23:14] So so far we've been focusing on IOPS
[23:16] because we wanted to look at the that
[23:18] issue we saw initially at the cost of
[23:21] doing very small IO. That's an issue we
[23:23] needed to solve. So all of our focus has
[23:25] been on reaching a higher mind of IOPS
[23:28] and doing efficient doing stuff
[23:29] efficiently at that level. But for a lot
[23:32] of other AI workloads bandwidth also a
[23:35] very relevant concern where it is
[23:38] feasible that the IO size does increase.
[23:41] And by that once you look at that then
[23:44] you see here a single GPU and on the on
[23:47] the left we have uh three NVME devices
[23:50] and with um and on the graph here you
[23:53] have the IO size and then bandwidth up
[23:55] here. Now at a very small IO size we're
[23:59] not saturating the bandwidth. As soon as
[24:02] we go up to 4K, three drives can easily
[24:05] be saturated can easily saturate the the
[24:08] PCE Gen 5 link of this GPU and
[24:11] increasing the the payload side even
[24:13] further doesn't really add a benefit and
[24:16] adding the fourth GPU uh sorry the
[24:19] fourth NVME drive doesn't really give
[24:21] you much. So the main takeaway from that
[24:24] is really that
[24:26] um there's a there's another big
[24:28] challenge which is we've been looking at
[24:30] software overhead unnecessary data
[24:32] copies and the challenge of getting all
[24:34] of this stuff to interoperate but
[24:36] there's also a big challenge in terms of
[24:38] C like a PC protocol over overhead and
[24:42] that's really what goes to waste here.
[24:45] So intuitively you might think that a
[24:47] BY6 GPU should be able to use four by
[24:51] four NVME drives but due to protocol
[24:54] overhead you actually only need three.
[24:57] And looking at this you can extrapolate
[25:00] that since with um since you need at 4K
[25:04] you need much less IO then with these
[25:06] efficiencies of IO at 4K you can
[25:09] saturate on a single CPU saturate 8 GPUs
[25:13] in terms of bandwidth.
[25:20] end here where what we wanted to
[25:23] demonstrate was this vision of being
[25:24] able to integrate the accelerators into
[25:27] the storage stack. And as you heard
[25:29] there are clear objections from Kristoff
[25:31] and I think we can uh discuss and see
[25:33] how we can address those but in general
[25:36] what we're looking at is having these
[25:38] different IO modes and see how we can
[25:40] integrate them with the existing
[25:42] software stack and figuring out what are
[25:44] the challenges. There are the advantages
[25:46] of doing IO very efficiently in a way
[25:49] where file systems, files and OS still
[25:52] exist and these fast path are executing
[25:54] on the side and it's all open source and
[25:57] either already upstream or targeting
[25:59] upstream and um on top of that uh yeah
[26:04] have a look at it. We just have some new
[26:06] device initiated experiments that I
[26:08] think have some pretty exciting numbers
[26:10] in them and the source code is available
[26:13] and so uh it's the white paper that goes
[26:15] into greater detail on what we've been
[26:17] doing and what we'll be doing from here
[26:19] on out. So yeah, I think that's that's
[26:22] it for me.
[26:24] So I hope you have uh questions.
[26:35] debugging tool. It has different content
[26:37] for different file systems. It's a
[26:39] massive risk for uh cost and corruption
[26:43] due to concurrent activity. That's why I
[26:45] told everyone including your boss two
[26:48] years ago, you need to expand the PFS
[26:50] block layout layouts that have all the
[26:52] mechanisms to deal with that including
[26:55] relocation mechanism mechanism for
[26:58] defending clients
[27:06] thank you Kristoff.
[27:08] So I think that was more a comment than
[27:09] a than a question and uh I think we'll
[27:12] take that into consideration. We also
[27:14] see a lot of benefits with stuff like
[27:16] PNF and the flex files and putting that
[27:19] as the management and the abstraction
[27:21] layer for these things. So, we're not
[27:24] using a fine map. Um, but we're
[27:26] definitely exploring what's what's out
[27:28] there and what's possible. And then, uh,
[27:31] yeah, any any other questions?
[27:46] that you've been providing, the metrics
[27:48] that you provided, are these files
[27:51] dynamically allocated or these files uh
[27:54] provisioned ahead of time? So, they're
[27:56] fixed size.
[27:58] &gt;&gt; Yeah, they're provisioned ahead of time.
[27:59] So the initial stuff that you saw here,
[28:03] oh
[28:16] the imageet data set some uh the tik tok
[28:19] data set and just some large uh 8
[28:21] gigabyte files so pre-allocated and we
[28:24] were not looking at right uh workloads
[28:27] entirely looking at how can we get is
[28:29] access to these files from a GPU.
[28:44] Oh, yeah.
[28:54] sequentially only or are they random uh
[28:57] accessed? they just read in into like in
[29:00] a data loader workload. So we took
[29:03] inspiration for that part from like Deli
[29:05] to be able to do a comparison to the
[29:08] Nvidia Deli framework where they use
[29:10] files as a in a data loader benchmark.
[29:13] So basically just making sure all of
[29:14] those you know images of cats are
[29:17] available to do whatever whatever
[29:19] analysis you need when you analyze
[29:21] images of cats and so forth. Yeah.
[29:25] Yeah.
[29:31] &gt;&gt; Okay. Thank you.
