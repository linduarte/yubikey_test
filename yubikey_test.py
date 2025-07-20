import subprocess

def check_yubikey_gpg():
    try:
        # Run the GPG command to list secret keys (YubiKey should be detected here)
        result = subprocess.run(
            ["gpg", "--card-status"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check if the YubiKey is detected
        if "YubiKey" in result.stdout:
            print("✅ YubiKey detected and GPG card status retrieved successfully.")
            print(result.stdout)
        else:
            print("⚠️ YubiKey not detected. Please ensure it is connected and configured.")
            print(result.stderr)

    except FileNotFoundError:
        print("❌ GPG is not installed or not found in the system PATH.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    check_yubikey_gpg()
