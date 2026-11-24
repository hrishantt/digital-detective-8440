# Mission 7 — how computers communicate

## 1. task / objective
learn basic network types and concepts, test connectivity and DNS lookup in terminal, and explain what happens when opening a website

## 2. work completed
- made a table of basic network concepts with simple examples
- tested network connection using `ping` and `nslookup`
- wrote a simple 7-step guide of how a web page opens

---

### task 7.1 — explain network concepts

| concept | explain it in your own words | example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | network in a small area | home Wi-Fi connecting laptop, phone and printer |
| **MAN (Metropolitan Area Network)** | network covering a city or large campus | university campus network |
| **WAN (Wide Area Network)** | network covering countries or the whole world | the internet |
| **DNS (Domain Name System)** | translates website name into an IP address | turning `example.com` into `104.20.23.154` |
| **Router** | device that connects networks and forwards data | home Wi-Fi broadband router |
| **Protocol** | set of rules devices follow to talk to each other | HTTP and HTTPS |
| **Packet switching** | splitting data into small packets to send across network | streaming a YouTube video |
| **Client-server** | client asks for service and server provides it | browser asking web page from web server |

---

### task 7.2 — observe network information
ran terminal commands for `example.com`:

```bash
ping -c 3 example.com
nslookup example.com
```

#### what i observed:
- **ping:** 3 packets sent, 3 received, 0% loss, average time around 10 ms
- **nslookup:** showed a `Non-authoritative answer` from server `8.8.8.8`, giving IP address `104.20.23.154` for `example.com`

#### questions answered:
- **what a connectivity test (`ping`) helps check:**
  it checks if a website or server is online, and how fast the connection responds
- **what a DNS lookup (`nslookup`) shows:**
  it shows the DNS server used and the IP address matching the website name
- **role of DNS when opening a website:**
  humans remember names like `example.com`, but computers only connect using numeric IP addresses. DNS finds the right IP address for the browser

---

### task 7.3 — what happens when you open a website?
1. you type the website URL in the browser (the client)
2. browser asks the DNS server to find the IP address of that website
3. DNS returns the server IP address to the browser
4. browser connects to the server and sets up a secure HTTPS connection
5. browser sends a request to the server for the web page files
6. the router sends the data packets between client and server
7. browser receives the files and displays the web page on the screen

---

## 3. commands / tools used
- `ping`: checked network connection and speed
- `nslookup`: checked website IP address using DNS

## 4. my understanding
the internet works by connecting clients (our computers) to servers (where websites live). DNS works like a contact list translating names to numbers, and routers move data packets back and forth

## 5. difficulties faced
understanding the difference between authoritative and non-authoritative DNS answers

## 6. how i resolved them
learned that non-authoritative simply means the DNS server gave a cached copy of the IP

## 7. evidence / files
- `evidence/mission-07/network_observations.txt`: ping and nslookup logs

## 8. commit details
- commit message: `complete networking and website steps mission`
- branch: `main`
- status: committed and pushed to github
