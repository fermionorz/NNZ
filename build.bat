@pyinstaller -F -w -i res\images\logo.png --distpath . nnz.py
@echo "PS C:\> certutil -hashfile nnz.exe [md5, SHA1, SHA256]" > Verification.txt
@certutil -hashfile dist/nnz.exe md5 | findstr /V CertUtil >> Verification.txt
@certutil -hashfile dist/nnz.exe sha1 | findstr /V CertUtil >> Verification.txt
@certutil -hashfile dist/nnz.exe sha256 | findstr /V CertUtil >> Verification.txt