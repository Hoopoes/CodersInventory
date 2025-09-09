# MinIO Installation Guide

MinIO is a high-performance, S3-compatible object storage system.
Follow the steps below to install and run it on Windows or Linux.


## 📥 Step 1 — Download MinIO

=== "Windows"
   
    1. Open **PowerShell** and create a folder for MinIO:

        ```powershell
        mkdir C:\MinIO
        cd C:\MinIO
        ```
    2. Download the latest MinIO server binary:
        
        [Download MinIO for Windows](https://www.min.io/open-source/download?platform=windows){:target="_blank" rel="noopener noreferrer"}
    
        ```powershell
        Invoke-WebRequest -Uri "https://dl.min.io/server/minio/release/windows-amd64/minio.exe" -OutFile "minio.exe"
        ```

=== "Linux"

    1. Download and install the MinIO package:

        [Download MinIO for Linux](https://www.min.io/open-source/download?platform=linux&arch=amd64){:target="_blank" rel="noopener noreferrer"}

        ```bash
        dnf install https://dl.min.io/server/minio/release/linux-amd64/minio-20250723155402.0.0-1.x86_64.rpm
        minio --version
        ```

## ▶️ Step 2 — Run MinIO Server

First, create a folder for storing MinIO data. Example: `C:\MinIO\data` (Windows) or `/data/minio` (Linux).

=== "Windows"

    ```powershell
    minio.exe server C:\MinIO\data
    ```

    With custom ports

    ```powershell
    minio.exe server C:\MinIO\data --address :9000 --console-address :9001
    ```

=== "Linux"

    ```bash
    sudo mkdir -p /data/minio
    sudo chown -R $USER:$USER /data/minio
    ```

    ```bash
    minio server /data/minio
    ```

    With custom ports

    ```bash
    minio server /data/minio --address :9000 --console-address :9001
    ```

* **9000** → S3 API endpoint
* **9001** → MinIO Web Console

Access console in browser:
👉 [http://localhost:9001](http://localhost:9001)


## ⚙️ Step 3 — Run MinIO as a Service

=== "Windows"

    This ensures MinIO starts automatically with Windows.

    1. Download the Windows Service helper:
    
        [MinIO Service Helper for Windows](https://github.com/minio/minio-service/tree/master/windows){:target="_blank" rel="noopener noreferrer"}
        
        ??? note "install-service.ps1"

            ```powershell title="install-service.ps1"
            #Check script run as administrator
            if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) { Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs; exit }

            Set-Location -Path $PSScriptRoot

            [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
            Invoke-WebRequest -Uri "https://github.com/winsw/winsw/releases/download/v2.8.0/WinSW.NET4.exe" -OutFile "minio-service.exe"

            $config = @'
            <service>
            <id>MinIO</id>
            <name>MinIO</name>
            <description>MinIO is a high performance object storage server</description>
            <executable>minio.exe</executable>
            <env name="MINIO_ROOT_USER" value="minio"/>
            <env name="MINIO_ROOT_PASSWORD" value="minio123"/>
            <arguments>server C:\minio</arguments>
            <logmode>rotate</logmode>
            </service>
            '@

            Set-Content "minio-service.xml" $config

            Start-Process -WorkingDirectory $PSScriptRoot -FilePath "$($PSScriptRoot)\minio-service.exe" -ArgumentList "install" -NoNewWindow -PassThru -Wait

            Write-Host "Installation done"
            ```

    2. Edit `install-service.ps1` (inside `C:\MinIO`) and set:

        * Path to `minio.exe`
        * Path to storage (`C:\MinIO\data`)
        * Credentials (optional)

        Example section inside script:

        ```xml
        <executable>minio.exe</executable>
        <env name="MINIO_ROOT_USER" value="minioadmin"/>
        <env name="MINIO_ROOT_PASSWORD" value="minioadmin123"/>
        <arguments>server C:\MinIO\data --address :9000 --console-address :9001</arguments>
        ```

    3. Run the installer script (in **PowerShell as Administrator**):

        ```powershell
        .\install-service.ps1
        ```

    4. Start the service:

        ```cmd
        net start MinIO
        ```

    5. Verify service status:

        ```cmd
        sc query MinIO
        ```

=== "Linux"

    1. Create service file:

        ```bash
        sudo nano /etc/systemd/system/minio.service
        ```

        Paste:

        ```ini
        [Unit]
        Description=MinIO Object Storage
        After=network.target

        [Service]
        User=root
        Group=root
        ExecStart=/usr/local/bin/minio server /data/minio --address :9000 --console-address :9001
        Environment="MINIO_ROOT_USER=minioadmin"
        Environment="MINIO_ROOT_PASSWORD=minioadmin123"
        Restart=always
        LimitNOFILE=65536

        [Install]
        WantedBy=multi-user.target
        ```

    2. Reload services & enable MinIO:

        ```bash
        sudo systemctl daemon-reload
        sudo systemctl enable minio
        sudo systemctl start minio
        ```

    3. Check status:

        ```bash
        systemctl status minio
        ```