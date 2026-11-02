# AIG Shields Up: Cybersecurity — Forage

A cybersecurity portfolio project by Darsh Rathi documenting the AIG Shields Up job simulation on Forage, completed in November 2026. The work covers researching Log4Shell, communicating remediation priorities, and recovering a password-protected ZIP in a controlled exercise.

This was an educational simulation, not employment or a production incident response engagement.

## Work included

| Deliverable | Purpose |
| --- | --- |
| [Log4j advisory email](docs/log4j-advisory.md) | Explain the vulnerability, identify the potentially affected staging environment, and request remediation and verification. |
| [Python dictionary attack script](bruteforce.py) | Try a supplied password list against the exercise ZIP and stop after successful extraction. |
| [Encrypted exercise archive](enc.zip) | Password-protected ZIP supplied for the Forage recovery exercise. |
| [Exercise password list](rockyou.txt) | Small RockYou subset supplied with the simulation, not the full RockYou wordlist. |

## Task 1: Vulnerability research and communication

I reviewed CISA's Log4j advisory and ransomware trends material, then used the simulation's infrastructure inventory to identify Product Development as the team to contact. Its staging environment explicitly listed Log4j; the inventory did not establish its version or prove compromise.

The advisory explains how CVE-2021-44228 can lead to remote code execution, the possible consequences, and the actions needed: inventory affected components, contain exposure, apply vendor-supported fixes, investigate potential exploitation, and verify remediation.

The source advisories date from 2021–2022. They provide the historical context for this exercise; their version-specific patch advice should not be treated as current production guidance.

## Task 2: Recovering the exercise archive

The simulated response team stopped a ransomware installation after one ZIP had been encrypted. I completed the supplied Python template to try passwords from the provided wordlist.

The script:

1. Opens `enc.zip` and reads `rockyou.txt` in binary mode.
2. Removes line endings while preserving the candidate password bytes.
3. Calls `attempt_extract()` for each candidate.
4. Continues after password, archive-integrity, or decompression errors.
5. Prints the successful password and extracts into `recovered/`, or reports that the list was exhausted.

Although the exercise calls this brute forcing, this implementation is specifically a **dictionary attack**. It tries listed candidates rather than generating every possible combination. It cannot guarantee recovery of arbitrary ransomware-encrypted files.

## Run locally

Requires Python 3 and its standard library; no third-party packages are needed.

The repository already includes `enc.zip` and the small `rockyou.txt` exercise wordlist alongside `bruteforce.py`. Clone the repository and run:

```sh
git clone https://github.com/drat-git/aig-forage-cybersecurity.git
cd aig-forage-cybersecurity
python3 bruteforce.py
```

The recovered document appears inside `recovered/`, which remains excluded from version control. No separate exercise-file download is needed. The script is scoped to the supplied exercise files; unsupported ZIP formats require separate handling.

## Verification

Checked locally against the supplied exercise pack in a temporary directory:

- An incorrect candidate was rejected and the exhausted-list message appeared.
- The supplied wordlist recovered the document, and the DOCX ZIP integrity check passed.
- The recovered document remained inside `recovered/`.

## Skills practiced

- Interpreting vulnerability advisories and distinguishing potential exposure from confirmed compromise.
- Matching affected software to system ownership.
- Writing actionable security communications for technical teams.
- Python file handling, byte strings, loops, exception handling, and ZIP extraction.
- Understanding the limits of password-list recovery.

## Sources and attribution

- [AIG Shields Up: Cybersecurity on Forage](https://www.theforage.com/simulations/aig/cybersecurity-ku1i): scenario and starter template.
- [CISA: Mitigating Log4Shell and Other Log4j-Related Vulnerabilities](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-356a).
- [CISA: Ransomware Trends from 2021](https://www.cisa.gov/news-events/news/cisa-fbi-nsa-and-international-partners-issue-advisory-ransomware-trends-2021).

The implementation and portfolio write-up were developed with AI assistance. The scenario and starter materials belong to their respective owners. This repository is a personal learning record and is not an official AIG or Forage publication. Use the script only with archives you own or are authorized to recover.
