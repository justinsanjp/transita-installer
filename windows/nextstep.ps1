# Python Installation Check and Download Script
Add-Type -AssemblyName System.Windows.Forms

# Function to check Python installation
function Test-PythonInstallation {
    try {
        $pythonVersion = python --version
        return $true
    }
    catch {
        return $false
    }
}

# Check if Python is installed
if (Test-PythonInstallation) {
    [System.Windows.Forms.MessageBox]::Show(
        "Python ist bereits installiert!`nVersion: $(python --version)",
        "Python Installation",
        [System.Windows.Forms.MessageBoxButtons]::OK,
        [System.Windows.Forms.MessageBoxIcon]::Information
    )
}
else {
    $result = [System.Windows.Forms.MessageBox]::Show(
        "Python ist nicht installiert.`n`nMöchten Sie Python jetzt herunterladen?`n`nKlicken Sie 'Ja', um zur Download-Seite zu gehen.",
        "Python nicht gefunden",
        [System.Windows.Forms.MessageBoxButtons]::YesNo,
        [System.Windows.Forms.MessageBoxIcon]::Warning
    )

    if ($result -eq 'Yes') {
        Start-Process "https://www.python.org/downloads/"
    }
}