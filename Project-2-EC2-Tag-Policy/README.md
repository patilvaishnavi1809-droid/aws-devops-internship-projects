# Project 2: EC2 Instance Launch with Enforced Tagging Policy

## 📌 Objective
Enforce mandatory tagging on every EC2 instance using **AWS Organizations Tag
Policies** (or an equivalent **Service Control Policy**), and demonstrate that
instances cannot be launched unless the required tags are supplied.

## 🏷 Required Tags
| Tag Key   | Example Value       |
|-----------|----------------------|
| Name      | Rahul                |
| emailID   | rahul@example.com    |
| phoneNo   | 9999999999           |
| Place     | Pune                 |

## 🛠 Tech Stack
`AWS Organizations` · `Tag Policies` · `Service Control Policies (SCP)` · `Amazon EC2` · `AWS CLI`

---

## 🚀 Step-by-Step Guide

### Step 1: Define the Tag Policy
1. Open [`policies/tag-policy.json`](policies/tag-policy.json) — this defines the
   four mandatory tag keys (`Name`, `emailID`, `phoneNo`, `Place`).
2. In **AWS Organizations Console → Policies → Tag policies**, create a new policy
   and paste the JSON in.
3. Attach the policy to the target Organizational Unit (OU) or account.

**✅ Deliverable:** Screenshot of the tag policy created in AWS Organizations.
📸 `screenshots/step1-tag-policy-created.png`

---

### Step 2: Enforce with a Service Control Policy (if Tag Policies alone aren't enough)
Tag Policies only **report** non-compliance by default — to actually **block**
launches, attach the SCP in [`policies/scp-deny-untagged-ec2.json`](policies/scp-deny-untagged-ec2.json)
to the same OU/account. It denies `ec2:RunInstances` unless all four tags are
present on the request.

**✅ Deliverable:** Screenshot of the SCP attached in the Organizations console.
📸 `screenshots/step2-scp-attached.png`

---

### Step 3: Launch an EC2 Instance WITH Required Tags (should succeed)
Run [`scripts/launch_ec2_with_tags.sh`](scripts/launch_ec2_with_tags.sh):
```bash
./scripts/launch_ec2_with_tags.sh
```
This should launch successfully because `Name`, `emailID`, `phoneNo`, and `Place`
are all supplied in `--tag-specifications`.

**✅ Deliverable:** Screenshot / CLI output of the successful instance launch.
📸 `screenshots/step3-launch-success.png`

---

### Step 4: Launch an EC2 Instance WITHOUT Tags (should fail)
Run [`scripts/launch_ec2_without_tags.sh`](scripts/launch_ec2_without_tags.sh):
```bash
./scripts/launch_ec2_without_tags.sh
```
Expected result — the call is rejected with an `UnauthorizedOperation` /
`Encoded authorization failure message` error, proving enforcement works.

**✅ Deliverable:** Screenshot / CLI output of the rejected launch attempt.
📸 `screenshots/step4-launch-failure.png`

---

### Step 5: Document Behavior & Reasoning
Summarize (in this README or a short report) *why* the second launch failed —
i.e., the SCP's `Null` condition evaluates to `true` when a required tag key is
absent from the request, triggering an explicit `Deny`.

**✅ Deliverable:** Written explanation (see [Security Considerations](#-how-enforcement-works) below).

---

## 📂 Repository Structure
```
Project-2-EC2-Tag-Policy/
├── README.md
├── policies/
│   ├── tag-policy.json
│   └── scp-deny-untagged-ec2.json
├── scripts/
│   ├── launch_ec2_with_tags.sh
│   └── launch_ec2_without_tags.sh
└── screenshots/
```

## 🔐 How Enforcement Works
The SCP statements use the `Null` IAM condition operator on
`aws:RequestTag/<key>`. When a tag key is **not** present in the `RunInstances`
request, `aws:RequestTag/<key>` is null, the condition evaluates to `true`, and
the matching `Deny` statement blocks the call — regardless of any `Allow`
elsewhere, since SCPs are guardrails that cap the maximum available permissions.

## ✅ Deliverables Checklist
- [ ] Description of the tag policy
- [ ] Screenshot of tag policy creation
- [ ] Screenshot of instance launch success with tags
- [ ] Screenshot of instance launch failure without tags
- [ ] Step-by-step guide for applying/enforcing tags (this README)
