@cd /d %~dp0
pyinstaller -F -w -i res\images\logo.png --distpath . nnz.py
@echo PS C:\> certutil -hashfile nnz.exe [md5, SHA1, SHA256] > Verification.txt
@echo -------------------------------------------------------------------------------- >> Verification.txt
@certutil -hashfile nnz.exe md5 >> Verification.txt
@echo -------------------------------------------------------------------------------- >> Verification.txt
@certutil -hashfile nnz.exe sha1 >> Verification.txt
@echo -------------------------------------------------------------------------------- >> Verification.txt
@certutil -hashfile nnz.exe sha256 >> Verification.txt
@echo -------------------------------------------------------------------------------- >> Verification.txt