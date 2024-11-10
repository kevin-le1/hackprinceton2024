# HealthSync

## Overview

HealthSync addresses a critical gap in healthcare coordination by establishing a secure, decentralized system that enables hospitals to prioritize patient cases and allocate practitioners across facilities—without compromising patient privacy or violating HIPAA regulations. In many healthcare settings, patient data remains siloed, complicating efforts to share real-time information across hospitals. This fragmentation results in inefficient specialist allocation, leading to treatment delays and, ultimately, poorer patient outcomes. HealthSync revolutionizes this by offering a privacy-preserving, decentralized network for hospitals to view and respond to high-priority cases globally.

## How It Works

HealthSync is a decentralized, consensus-driven network that assigns urgency scores to patients based on encrypted medical data, using a large language model (LLM) and secure data sharding. Patient data is processed across peer-to-peer (P2P) nodes, generating a global urgency ranking that appears on a real-time dashboard, helping hospitals prioritize high-risk cases efficiently and securely.

## Workflow

- Node Integration: New hospitals join by connecting to neighboring nodes, forming a fully integrated P2P network.
Urgency Calculation: Each hospital queries its local database for patient information and assigns urgency scores (0-100) through an LLM, triggering network-wide urgency calculations.
- Data Security: Patient data is encrypted and divided using Shamir’s Secret Sharing (SSS), with fragments distributed across nodes to ensure privacy.
- Global Ranking via SMC: Using Secure Multi-Party Computation (SMC), nodes exchange and process data shards to produce a secure, combined urgency ranking without exposing any original data.
- Dashboard and Specialist Allocation: A global urgency ranking is displayed on the dashboard, enabling real-time specialist allocation and data-driven decision-making across facilities.
Use Case
- HealthSync can play a vital role in promoting cell therapy education and boosting clinical trial enrollment by securely connecting patients and physicians in a decentralized network that respects patient privacy. For example, when a patient shows interest in cell therapy, their data—including medical history and physician notes—can be processed through HealthSync's network to assess their eligibility and urgency for clinical trials. Hospitals across the network receive a secure, real-time ranking of potential trial participants without revealing personal details, ensuring a streamlined, HIPAA-compliant approach to patient outreach.

## Impact and Benefits

HealthSync ensures a compliant, secure approach to resource allocation, upholding HIPAA requirements by protecting patient data throughout the process. Through encryption, sharding, and SMC, HealthSync enables hospitals to act on a unified, global view of patient urgency, optimizing treatment allocation without sacrificing privacy. This architecture advances healthcare efficiency, reduces costs, and improves access to urgent care, offering a tangible, privacy-respecting solution to fragmented healthcare systems.

## Technologies

The P2P network was developed from the ground up using WebSocket for connectivity. Data security is achieved through Shamir’s Secret Sharing (SSS) and Secure Multi-Party Computation (SMC) libraries. The React-based frontend interfaces with SQL databases for efficient data handling, and computations are executed using Ollama for optimized performance across systems.

## How to Run

We use `poetry` to manage our Python environment and packages. Be sure to configure your .env (look at .example.env) before running.

### Genesis Server

Run `python genesis-node/server.py`

### Local Server

Run `flask run --port=8000 --host={YOUR_IP}`. Under the hood, this leverages a p2p overlay network to enable decentralized compute and consensus.

### Website

Run `yarn dev`
