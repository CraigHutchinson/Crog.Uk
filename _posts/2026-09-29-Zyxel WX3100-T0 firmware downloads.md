---
layout: post
title:  "Zyxel EX3301-T0 and WX3100-T0 firmware downloads"
date:   2026-09-29 12:00:00 +0000
modified_date: 2026-11-18 12:00:00 +0000
categories: Networking
---

Zyxel's **EX3301-T0** router and **WX3100-T0** access point/extender are both service-provider
products, so neither has firmware in the consumer
[Download Library](https://www.zyxel.com/uk/en-gb/support/download?model=wx3100-t0). That page serves
only manuals, the quick start guide, datasheets and CE declarations, and Zyxel's security advisories
direct you to a sales representative for patch files.

The firmware is nonetheless on Zyxel's public CDN, unauthenticated and unlisted. This note collects
the current builds, the URL schemes that reach them, and how to probe for new ones.

## Latest firmware

| Product | Role | Latest build | Size | Published | Download |
| :------ | :--- | :----------- | ---: | :-------- | :------- |
| EX3301-T0 | Router | `5.50(ABVY.7.2)C0` | 31.5&nbsp;MB | 14 Jul 2026 | [zip](https://download.zyxel.com/EX3301-T0/firmware/EX3301-T0_5.50%28ABVY.7.2%29C0.zip) |
| WX3100-T0 | AX1800 access point / extender | `5.50(ABVL.5.2)C0` | 18.9&nbsp;MB | 29 Sep 2026 | [zip](https://download.zyxel.com/WX3100-T0/firmware/WX3100-T0_5.50%28ABVL.5.2%29C0.zip) |

- **WX3100-T0 advisory build.** Zyxel's
  [21 July 2026 advisory](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-post-authentication-command-injection-vulnerability-in-certain-dsl-ethernet-cpe-fiber-onts-and-wireless-extenders-07-21-2026)
  (CVE-2026-6952, post-authentication command injection in the syslog `LogServer` field) names
  `5.50(ABVL.5.1)C0` as the patch. That build is still published at
  [`WX3100-T0_5.50%28ABVL.5.1%29C0.zip`](https://download.zyxel.com/WX3100-T0/firmware/WX3100-T0_5.50%28ABVL.5.1%29C0.zip).
  No advisory names `5.2` yet, so whether it carries the CVE fix is unverified. Use `5.1` if that
  specific build is required.
- **EX3301-T0 mirror.** The same build is also at the router-style `spdl` path, which is dated
  28 April 2026. Prefer the `download` host.

## URL schemes

Both products share one CDN, but the layout depends on which host a file was published under:

| Product | Host | Path | Filename |
| :------ | :--- | :--- | :------- |
| EX3301-T0 | `download.zyxel.com` | `/EX3301-T0/firmware/` | `EX3301-T0_{VERSION}.zip` |
| WX3100-T0 | `download.zyxel.com` | `/WX3100-T0/firmware/` | `WX3100-T0_{VERSION}.zip` |
| DX3300-T0 (router sibling) | `spdl.zyxel.com` | `/DX3300-T0/firmware(public_version)/` | `DX3300-T0_Firmware_{VERSION}.zip` |

The trap is that the router-style `spdl` URL does not convert to the extender by swapping the model
name. Three things change together: the host `spdl` becomes `download`, the folder
`firmware(public_version)` becomes `firmware`, and the `_Firmware_` infix is dropped.

Model codes are not interchangeable either. **ABVL** is the WX3100-T0 and **ABVY** is the
DX3301/DX3300/EX3301/EX3300-T0 family. Mixing them produces plausible-looking URLs that do not exist.

## WX3100-T0 builds

| Version | Size | Published |
| :------ | ---: | :-------- |
| 5.50(ABVL.0)C0 | 15.5&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVL.1.1)C0 | 15.8&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVL.4)C0 | 17.6&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVL.4.1)C0 | 17.6&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVL.4.2)C0 | 17.6&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVL.4.3)C0 | 17.6&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVL.4.4)C0 | 17.6&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVL.4.6)C0 | 17.7&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVL.4.7)C0 | 17.7&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVL.4.8)C0 | 18.3&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVL.4.9)C0 | 18.0&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVL.5)C0 | 18.9&nbsp;MB | 14 Jul 2026 |
| 5.50(ABVL.5.1)C0 | 18.7&nbsp;MB | 14 Jul 2026 |
| **5.50(ABVL.5.2)C0** | **18.9&nbsp;MB** | **29 Sep 2026** |

Confirmed **absent**: `4.5`, `4.10`, `4.11`+, `5.3`+, `6.x`, any `5.70` build, and the `Y0` suffix
variants.

The advisory of
[28 April 2026](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-command-injection-vulnerabilities-in-certain-4g-lte-5g-nr-cpe-dsl-ethernet-cpe-fiber-onts-and-wireless-extenders-04-28-2026)
(CVE-2026-0711) names **4.10** as its patch, but that build was never published. `5.1` supersedes it.
The user's guide covers "V5.17_5.70", but no 5.70 firmware exists for this model.

## EX3301-T0 builds

| Version | Size | Published |
| :------ | ---: | :-------- |
| 5.50(ABVY.4)C0 | 27.9&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVY.6.2)C0 | 30.2&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVY.6.4)C0 | 30.6&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVY.7)C0 | 31.5&nbsp;MB | 10 Apr 2026 |
| 5.50(ABVY.7.1)C0 | 31.5&nbsp;MB | 14 Jul 2026 |
| **5.50(ABVY.7.2)C0** | **31.5&nbsp;MB** | **14 Jul 2026** |

Confirmed **absent**: any `8.x` or `9.x` build, and the `ABVY.6` minors other than `6.2` and `6.4`.
The search covered every `ABVY.6` to `ABVY.9` minor and sub-minor on both hosts, so a newer build
would have to use a different naming scheme to be found this way.

## Probing for future releases

The CDN returns **HTTP 200 for missing files**, serving a 114-byte HTML redirect stub. Status codes
are therefore useless for existence checks. Test the `Content-Type` instead: a real file is
`application/x-zip-compressed` and a miss is `text/html`.

```bash
probe() {
  url="https://download.zyxel.com/$1/firmware/$1_$2.zip"
  ct=$(curl -sI -m 10 --globoff "$url" | tr -d '\r' | awk 'tolower($1)=="content-type:"{print $2}')
  cl=$(curl -sI -m 10 --globoff "$url" | tr -d '\r' | awk 'tolower($1)=="content-length:"{print $2+0}')
  [ "$ct" = "application/x-zip-compressed" ] &&
    awk -v v="$2" -v c="$cl" 'BEGIN{printf "%-32s %.1f MB\n", v, c/1048576}'
}

probe WX3100-T0 "5.50(ABVL.5.3)C0"
probe EX3301-T0 "5.50(ABVY.8)C0"
```

Sanity-check any hit with a 4-byte range request before trusting it. A genuine archive starts
`PK\003\004`:

```bash
curl -s --globoff -r 0-3 \
  "https://download.zyxel.com/WX3100-T0/firmware/WX3100-T0_5.50%28ABVL.5.2%29C0.zip" | od -c
```

## Before you flash

**Read the current version first**, from the device's web UI under **Maintenance &rarr; Firmware
Upgrade**. The WX3100-T0 defaults to `http://192.168.1.2`.

**Check the suffix letter.** Every public build I found is **`C0`** (generic). Older `Y0` builds
exist for the WX3100-T0, such as `5.50(ABVL.2.1)Y0`, and those are ISP-customised images. A unit
running a non-`C0` build is on an ISP's own track, is typically updated only via TR-069, and will
often refuse a generic image outright. If one device on a network has stayed behind while its
siblings updated, check this first. I have not swept for `Y0` builds on the EX3301-T0.

**WX3100-T0: mind the gap below 4.** The size jumps from 15.8&nbsp;MB at `1.1` to 17.6&nbsp;MB at `4`,
with **no 2.x or 3.x build published at all**. That discontinuity suggests a platform change across
the boundary. Upgrading from `0` or `1.1` may work directly, but if `5.2` is rejected, stage it
`1.1` &rarr; `4.7` &rarr; `5.2`. Devices already on the 4.x line go straight to `5.2`.

**WX3100-T0: risk context.** WAN management is disabled by default and CVE-2026-6952 requires
authenticated administrator access, so a stable, unexposed device on an older build faces mild
urgency. Weigh that against reports of instability on the
[`4.4` build](https://community.zyxel.com/en/discussion/28374/issue-with-zyxel-wx3100-t0-firmware-5-50-abvl-4-4-c0).

## WX3100-T0 and OpenWrt

There is no third-party route. The
[OpenWrt support thread](https://forum.openwrt.org/t/support-for-zyxel-wx3100-t0/166003) documents
the hardware (ECONET EN7516GT SoC, 256&nbsp;MB RAM, 128&nbsp;MB W25N01G flash, MediaTek MT7975DN and
MT7905DEN radios, UART pins populated by default), but the SoC is unsupported and a moderator's
verdict is that support is "not going to happen". Zyxel's own CDN is the only source of images.

---

*These are Zyxel's own unauthenticated CDN URLs, not mirrors. They are unlisted rather than secret,
so Zyxel can move or withdraw them without notice. If a link here dies, re-run the probe above
rather than assuming the build is gone.*
