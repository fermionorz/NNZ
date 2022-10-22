@certutil -hashfile dist/nnz.exe md5 | findstr /V CertUtil
@certutil -hashfile dist/nnz.exe sha1 | findstr /V CertUtil
@certutil -hashfile dist/nnz.exe sha256 | findstr /V CertUtil
pause