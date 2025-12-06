# Matter/Thread TUI - Story Map

## User Story
**As a** Matter/Thread network owner
**I need to** see and manage my devices
**So that** I can understand what's happening and fix problems

---

## Overall Story Map - User Journey Backbone

```mermaid
graph TB
    subgraph "USER ACTIVITIES - The Backbone"
        A1["🔍 Discover<br/>My Devices"]
        A2["👁️ Monitor<br/>Health"]
        A3["🔧 Troubleshoot<br/>Issues"]
        A4["⚙️ Control<br/>Devices"]

        A1 --> A2 --> A3 --> A4
    end

    subgraph "RELEASE 1 - Walking Skeleton"
        R1A["List devices<br/>I have"]
        R1B["See basic<br/>status"]
    end

    subgraph "RELEASE 2 - See Problems"
        R2A["Search for<br/>specific device"]
        R2B["Identify<br/>offline devices"]
        R2C["View error<br/>messages"]
    end

    subgraph "RELEASE 3 - Fix Problems"
        R3A["View device<br/>details"]
        R3B["Test device<br/>connectivity"]
        R3C["Send basic<br/>commands"]
    end

    subgraph "RELEASE 4 - Understand Network"
        R4A["See network<br/>topology"]
        R4B["View signal<br/>strength"]
        R4C["See device<br/>relationships"]
    end

    subgraph "RELEASE 5 - Manage Fabrics"
        R5A["View fabrics"]
        R5B["Commission<br/>new device"]
        R5C["Remove from<br/>fabric"]
    end

    R1A -.-> A1
    R1B -.-> A2

    R2A -.-> A1
    R2B -.-> A2
    R2C -.-> A3

    R3A -.-> A1
    R3B -.-> A3
    R3C -.-> A4

    R4A -.-> A1
    R4B -.-> A2
    R4C -.-> A2

    R5A -.-> A1
    R5B -.-> A4
    R5C -.-> A4

    style A1 fill:#e1f5ff
    style A2 fill:#fff9e1
    style A3 fill:#ffe1e1
    style A4 fill:#e1ffe1
```

---

## Release 1: Walking Skeleton
**Value: "Can I see what devices I have?"**

### The Simplest Thing That Could Possibly Work

```mermaid
graph LR
    subgraph "User Opens App"
        Start["Launch TUI"]
    end

    subgraph "Discover My Devices"
        S1["See list of<br/>device names"]
        S2["Count total<br/>devices"]
    end

    subgraph "Monitor Health"
        S3["See online/<br/>offline status"]
    end

    Start --> S1
    S1 --> S2
    S1 --> S3

    style Start fill:#90EE90
    style S1 fill:#87CEEB
    style S2 fill:#87CEEB
    style S3 fill:#FFD700
```

**User Stories:**
1. ✅ See a list of my device names
2. ✅ Know how many devices I have
3. ✅ See which devices are online/offline

**Implementation:**
- Single view: Device list
- Connect to python-matter-server
- Display: Name | Type | Status
- No navigation, no details, no controls

**Done When:**
- I launch the app
- I see my devices listed
- I can tell what's online

---

## Release 2: See Problems
**Value: "Can I identify what's broken?"**

```mermaid
graph LR
    subgraph "Discover My Devices"
        D1["Search/filter<br/>devices"]
        D2["Sort by name<br/>or status"]
    end

    subgraph "Monitor Health"
        M1["Highlight<br/>offline devices"]
        M2["Show last<br/>seen time"]
        M3["Display signal<br/>strength (RSSI)"]
    end

    subgraph "Troubleshoot Issues"
        T1["View error<br/>log"]
        T2["See connection<br/>failures"]
    end

    D1 --> M1
    D2 --> M1
    M1 --> M2
    M1 --> M3
    M2 --> T1
    M3 --> T1
    T1 --> T2

    style D1 fill:#87CEEB
    style D2 fill:#87CEEB
    style M1 fill:#FFD700
    style M2 fill:#FFD700
    style M3 fill:#FFD700
    style T1 fill:#FFA07A
    style T2 fill:#FFA07A
```

**User Stories:**
1. ✅ Find a specific device quickly
2. ✅ See which devices are offline
3. ✅ Know when device was last seen
4. ✅ See signal strength problems
5. ✅ View recent errors

**Added to Release 1:**
- Search box
- Sort toggle
- RSSI column
- "Last Seen" timestamp
- Simple log viewer (bottom panel)
- Color coding (green=online, red=offline, yellow=weak signal)

**Done When:**
- I can type to search
- Offline devices stand out visually
- I can see the error log
- I know which device has weak signal

---

## Release 3: Fix Problems
**Value: "Can I take action on issues?"**

```mermaid
graph LR
    subgraph "Discover My Devices"
        D1["Select device<br/>for details"]
    end

    subgraph "Troubleshoot Issues"
        T1["View full<br/>device info"]
        T2["Ping device"]
        T3["Check<br/>connectivity"]
    end

    subgraph "Control Devices"
        C1["Toggle device<br/>on/off"]
        C2["Send test<br/>command"]
        C3["Read device<br/>attributes"]
    end

    D1 --> T1
    T1 --> T2
    T2 --> T3
    T1 --> C1
    C1 --> C2
    T1 --> C3

    style D1 fill:#87CEEB
    style T1 fill:#FFA07A
    style T2 fill:#FFA07A
    style T3 fill:#FFA07A
    style C1 fill:#90EE90
    style C2 fill:#90EE90
    style C3 fill:#90EE90
```

**User Stories:**
1. ✅ Select a device to see details
2. ✅ View all device attributes
3. ✅ Ping a device to test connectivity
4. ✅ Turn a device on/off
5. ✅ Send a simple command

**Added to Release 2:**
- Device detail panel (press Enter on device)
- Attributes viewer
- Ping tool (keyboard shortcut 'p')
- Basic controls (for lights/switches)
- Command result feedback

**Done When:**
- I can click/select a device
- I see manufacturer, model, capabilities
- I can ping to test connection
- I can turn my light on/off
- I know if command succeeded

---

## Release 4: Understand Network
**Value: "Can I see how devices connect?"**

```mermaid
graph LR
    subgraph "Discover My Devices"
        D1["View network<br/>topology"]
        D2["See border<br/>routers"]
    end

    subgraph "Monitor Health"
        M1["View device<br/>relationships"]
        M2["See routing<br/>paths"]
        M3["Monitor network<br/>health metrics"]
    end

    subgraph "Troubleshoot Issues"
        T1["Identify isolated<br/>devices"]
        T2["Find weak<br/>links"]
        T3["Trace route<br/>to device"]
    end

    D1 --> M1
    D2 --> M1
    M1 --> M2
    M2 --> M3
    M1 --> T1
    M2 --> T2
    M3 --> T1
    T2 --> T3

    style D1 fill:#87CEEB
    style D2 fill:#87CEEB
    style M1 fill:#FFD700
    style M2 fill:#FFD700
    style M3 fill:#FFD700
    style T1 fill:#FFA07A
    style T2 fill:#FFA07A
    style T3 fill:#FFA07A
```

**User Stories:**
1. ✅ See Thread network topology
2. ✅ Identify border routers
3. ✅ Understand parent-child relationships
4. ✅ Find routing paths
5. ✅ See network health statistics
6. ✅ Identify weak signal paths

**Added to Release 3:**
- Network view tab
- Topology visualization
- Border router highlighting
- Network stats panel
- Route tracing tool

**Done When:**
- I can switch to Network tab
- I see a visual graph of connections
- Border routers are clearly marked
- I can see which devices are routers vs. sleepy end devices
- I can trace path from border router to device

---

## Release 5: Manage Fabrics
**Value: "Can I manage device sharing?"**

```mermaid
graph LR
    subgraph "Discover My Devices"
        D1["View fabric<br/>membership"]
        D2["See which ecosystems<br/>control device"]
    end

    subgraph "Control Devices"
        C1["Commission<br/>new device"]
        C2["Remove device<br/>from fabric"]
        C3["Share device<br/>across fabrics"]
    end

    D1 --> D2
    D2 --> C1
    D1 --> C2
    D2 --> C3

    style D1 fill:#87CEEB
    style D2 fill:#87CEEB
    style C1 fill:#90EE90
    style C2 fill:#90EE90
    style C3 fill:#90EE90
```

**User Stories:**
1. ✅ See which fabrics control each device
2. ✅ View all fabrics (Apple Home, Google Home, etc.)
3. ✅ Commission a new device
4. ✅ Remove device from a fabric
5. ✅ See fabric overlap

**Added to Release 4:**
- Fabrics view tab
- Fabric tree view
- Commission wizard
- Remove from fabric action
- Fabric details panel

**Done When:**
- I can see all my fabrics
- I know which devices are shared
- I can add a new device via setup code
- I can remove a device from specific fabric
- I understand fabric relationships

---

## Priority Matrix

```mermaid
graph TB
    subgraph "MUST HAVE - Release 1"
        M1["List devices"]
        M2["Show online/offline"]
        M3["Basic TUI"]
    end

    subgraph "SHOULD HAVE - Release 2-3"
        S1["Search/filter"]
        S2["Device details"]
        S3["Basic control"]
        S4["Error visibility"]
    end

    subgraph "COULD HAVE - Release 4-5"
        C1["Network topology"]
        C2["Fabric management"]
        C3["Advanced diagnostics"]
    end

    subgraph "WON'T HAVE - Future"
        W1["Automation rules"]
        W2["Historical graphs"]
        W3["Firmware updates"]
    end

    style M1 fill:#ff6b6b
    style M2 fill:#ff6b6b
    style M3 fill:#ff6b6b
    style S1 fill:#ffd93d
    style S2 fill:#ffd93d
    style S3 fill:#ffd93d
    style S4 fill:#ffd93d
    style C1 fill:#6bcf7f
    style C2 fill:#6bcf7f
    style C3 fill:#6bcf7f
    style W1 fill:#a8dadc
    style W2 fill:#a8dadc
    style W3 fill:#a8dadc
```

---

## Implementation Sequence (Simplest First)

### Sprint 1: Walking Skeleton (Release 1)
**Goal: See my devices - that's it!**

```
Day 1-2: Basic Textual app with one screen
Day 3-4: Connect to python-matter-server
Day 5-6: Display device list with status
Day 7: Polish and test
```

**Demo:** "Look, here are my 12 devices, 10 online, 2 offline"

### Sprint 2: Visibility (Release 2)
**Goal: Find problems fast**

```
Day 1-2: Add search and sort
Day 3-4: Add RSSI and last-seen
Day 5-6: Add log viewer
Day 7: Color coding and polish
```

**Demo:** "I can instantly see my bedroom bulb is offline with weak signal"

### Sprint 3: Action (Release 3)
**Goal: Fix what's broken**

```
Day 1-2: Device detail panel
Day 3-4: Ping tool
Day 5-6: Basic device controls
Day 7: Command feedback
```

**Demo:** "I can ping the device, see it's reachable, and turn it on"

### Sprint 4: Understanding (Release 4)
**Goal: See the network structure**

```
Day 1-3: Thread network integration
Day 4-6: Topology visualization
Day 7: Network statistics
```

**Demo:** "I can see my 2 HomePod border routers and how devices connect"

### Sprint 5: Management (Release 5)
**Goal: Control fabrics**

```
Day 1-3: Fabric view
Day 4-6: Commission workflow
Day 7: Remove from fabric
```

**Demo:** "I can add a new device and share it across ecosystems"

---

## Value Per Release

| Release | User Value | Effort | ROI |
|---------|-----------|--------|-----|
| R1: Walking Skeleton | Can see what I have | 1 week | ⭐⭐⭐⭐⭐ |
| R2: See Problems | Can identify issues | 1 week | ⭐⭐⭐⭐⭐ |
| R3: Fix Problems | Can take action | 1 week | ⭐⭐⭐⭐ |
| R4: Network View | Can understand topology | 2 weeks | ⭐⭐⭐ |
| R5: Fabric Mgmt | Can manage sharing | 1 week | ⭐⭐⭐ |

**Key Insight:** Releases 1-3 deliver 80% of the value in 3 weeks. That's the target.
