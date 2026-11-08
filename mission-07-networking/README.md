# Mission 7 — How computers communicate

## 1. Task / objective
The objective of this mission is to explore fundamental computer networking principles, examine the core network topologies and protocols that power the global Internet, observe real-world network connectivity and DNS resolution using command-line diagnostic tools, and formulate an architectural step-by-step model of web communications.

## 2. Work completed
- Constructed a comprehensive network concepts reference table defining LAN, MAN, WAN, DNS, Routers, Protocols, Packet Switching, and Client-Server architecture.
- Executed terminal network diagnostics (`ping` and `nslookup`) against `example.com`, analyzing round-trip latency, packet loss, and IP resolution.
- Formulated an in-depth, 7-step technical lifecycle explaining what happens when a user requests a website in a web browser.
- Maintained strict privacy compliance by redacting local router IP addresses, Wi-Fi identifiers, and private network parameters.

---

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A communication network connecting computers and devices over a restricted, short-range geographic zone such as a home, school computer laboratory, or single office building. | A home Wi-Fi network connecting laptops, smartphones, and a wireless network printer. |
| **MAN (Metropolitan Area Network)** | A high-bandwidth network that spans an entire metropolitan municipal region or university campus, larger than a LAN but geographically smaller than a WAN. | A municipal fiber-optic ring interconnecting municipal government offices, police departments, and public libraries across a city. |
| **WAN (Wide Area Network)** | A large-scale telecommunications network covering expansive geographical regions across states, nations, continents, or the entire planet. | The global public Internet, or an international banking network linking branches worldwide. |
| **DNS (Domain Name System)** | A decentralized, hierarchical naming system that functions as the Internet's directory service, translating human-friendly domain names into machine-routable numeric IP addresses. | Resolving `example.com` into IPv4 address `104.20.23.154`. |
| **Router** | A specialized network gateway hardware device that inspects incoming data packet IP headers and forwards them across differing network segments toward their destination based on routing tables. | A broadband home fiber/Wi-Fi router routing data between private local subnet devices and the public Internet Service Provider (ISP) gateway. |
| **Protocol** | A standardized set of predetermined rules, syntactical formats, handshakes, and error-handling procedures that govern how computing devices exchange data across a network. | **HTTPS** (Hypertext Transfer Protocol Secure), **TCP** (Transmission Control Protocol), and **IP** (Internet Protocol). |
| **Packet switching** | A networking paradigm where digital data streams are segmented into smaller discrete blocks called packets, routed independently across dynamic network paths, and reassembled in proper sequence at the destination. | Streaming a 4K video stream on YouTube, where segments travel through various intermediate routers and are seamlessly reordered by the receiving browser. |
| **Client-server** | A distributed computing architecture dividing tasks between service requesters (clients) and centralized service providers (servers). | A web browser (client) requesting an HTML document from an Nginx or Apache web server hosting the website. |

---

### Task 7.2 — Observe network information
Terminal diagnostics were executed targeting the public test domain `example.com`:

```bash
# ICMP Connectivity Test
ping -c 3 example.com

# DNS Resolution Query
nslookup example.com
```

#### Observations:
- **Ping Output:**
  ```text
  PING example.com (104.20.23.154): 56 data bytes
  64 bytes from 104.20.23.154: icmp_seq=0 ttl=58 time=5.817 ms
  64 bytes from 104.20.23.154: icmp_seq=1 ttl=58 time=5.671 ms
  64 bytes from 104.20.23.154: icmp_seq=2 ttl=58 time=18.730 ms

  --- example.com ping statistics ---
  3 packets transmitted, 3 packets received, 0.0% packet loss
  round-trip min/avg/max/stddev = 5.671/10.073/18.730/6.122 ms
  ```
- **NSLookup Output:**
  ```text
  Server:     8.8.8.8
  Address:    8.8.8.8#53

  Non-authoritative answer:
  Name:       example.com
  Address:    104.20.23.154
  Name:       example.com
  Address:    172.66.147.243
  ```

#### Analysis:
- **What a connectivity test (`ping`) helps you check:**
  A connectivity test uses Internet Control Message Protocol (ICMP) Echo Request and Echo Reply messages to verify two critical networking indicators:
  1. *End-to-end reachability:* Confirms whether the destination host is online and reachable through the intervening network route.
  2. *Latency and stability:* Measures round-trip time (RTT in milliseconds) and detects packet loss percentage, indicating connection quality and network congestion.
- **What information a DNS lookup (`nslookup`) displays:**
  A DNS lookup reveals the resolving DNS nameserver answering the request (e.g., Google Public DNS `8.8.8.8` on port 53), the query response type (Authoritative vs. Non-authoritative), and the canonical resource records mapping the queried domain name to its public IPv4 (`A` records) and IPv6 (`AAAA` records) addresses.
- **The role of DNS when entering a website name in a browser:**
  While humans intuitively navigate the web using alphanumeric names like `example.com`, network routers, switches, and IP layer protocols operate exclusively on numeric binary IP addresses. When a user enters a URL, DNS acts as an instantaneous directory service, translating the human-readable domain into the destination server's machine-addressable IP so that network packets can be addressed and routed correctly.

---

### Task 7.3 — What happens when you open a website?
The complete lifecycle from user keystroke to rendered web page proceeds through seven distinct technical phases:

1. **Client Initiation & URL Parsing:**
   The user types `https://example.com` into the web browser (the **client**). The browser decomposes the URL into its constituent components: the application-layer **protocol** (`HTTPS`), the host domain name (`example.com`), and the default target port (`443`).
2. **DNS Resolution:**
   The client must determine the destination IP address. It checks its local browser cache, OS resolver cache, and if unresolved, sends a recursive **DNS** query over UDP/53 across the local router to the configured DNS server. The DNS server resolves `example.com` to public IP address `104.20.23.154`.
3. **TCP Connection Establishment (Three-Way Handshake):**
   Using the resolved IP address, the client initiates a reliable transport-layer connection with the remote **server**. The client and server execute a three-way TCP handshake (SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK) to synchronize sequence numbers and establish a persistent full-duplex communication channel.
4. **TLS Cryptographic Handshake:**
   Because the secure HTTPS **protocol** is requested, the client and server negotiate Transport Layer Security (TLS). The server presents its digital certificate verifying its cryptographic identity, and both parties negotiate symmetric encryption session keys to guarantee data privacy and tamper-resistance.
5. **HTTP Request Transmission & Router Packet Switching:**
   The client constructs an HTTP `GET /` request message asking for the root web page. The OS segments this message into TCP segments and IP packets. The local network **router** inspects each packet's destination header and uses packet switching to forward the packets across intermediate autonomous systems and fiber backbones to the target server.
6. **Server Processing & Response Generation:**
   The web **server** (e.g., Nginx, Cloudflare edge, or Apache) accepts the incoming HTTP request. The server validates headers, processes backend application logic or fetches static files, and generates an HTTP response consisting of a status code (`200 OK`), content headers (`Content-Type: text/html`), and the HTML payload.
7. **Client Rendering & Visual Presentation:**
   The server transmits the response packets back across the network to the client. The browser's rendering engine parses the incoming HTML document, downloads referenced CSS stylesheets, scripts, and image assets, constructs the Document Object Model (DOM) and Render Tree, and paints the final interactive web page onto the user's screen.

---

## 3. Commands / tools used
- `ping`: Diagnosed ICMP packet transmission, round-trip latency, and connection stability.
- `nslookup`: Performed DNS address resolution and nameserver query verification.

## 4. My understanding
Computer networking relies on a layered model of abstractions (such as the OSI and TCP/IP models). The client-server paradigm decouples resource presentation (the browser) from data hosting (the server), while DNS bridges human linguistic memory with binary numeric routing. Packet switching ensures resilient, distributed communication where independent packets dynamically traverse diverse pathways across interconnected routers.

## 5. Difficulties faced
Distinguishing between authoritative and non-authoritative DNS lookup responses in `nslookup`.

## 6. How I resolved them
Researched DNS architecture to learn that a "Non-authoritative answer" indicates the responding DNS resolver answered the query from its cached records rather than being the master authoritative nameserver holding the original zone configuration file.

## 7. Evidence / files
- `evidence/mission-07/network_observations.txt`: Captured logs of ping latency metrics and nslookup IP resolution.

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
- Branch: `main`
- Status: Staged and committed locally.
