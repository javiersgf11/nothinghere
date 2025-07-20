import windowspowershell as wps

wps = wps.WindowsPowerShell()

def run_powershell_script(script):
    try:
        # Create a PowerShell instance
        ps = wps.PowerShell()
        # Run the script
        ps.run_script(script)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ps.close()