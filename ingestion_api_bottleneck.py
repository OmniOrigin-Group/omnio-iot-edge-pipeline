# ========================================================================
# 🚨 CRITICAL API BOTTLENECK: DIRECT SYNCHRONOUS WRITE (DO NOT USE)
# Engineered by: OmniOrigin Group of Businesses
# Architecture: Legacy Blocking I/O Loop
# ========================================================================

import time

def handle_sensor_ingest_naive(payload):
    """
    This structure blocks the connection pool by waiting for heavy 
    disk writes synchronously for every single hardware alert packet.
    """
    print(f"[*] Extracting packet from node: {payload.get('device_id')}")
    
    # ❌ CRITICAL ERROR: Synchronous DB connection blocks the HTTP thread
    # Under a spike of 10k users/nodes, this causes 504 Gateway Timeouts
    time.sleep(2.4) # Simulating heavy disk database I/O latency
    
    print("[+] DB Write completed successfully.")
    return {"status": "success", "code": 201}
