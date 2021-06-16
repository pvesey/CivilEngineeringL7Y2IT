$Assignment1 = [PSCustomObject]@{
    Name = 'ITBM01-LIT-00-ZZ-SP-S-001-A1-P01'
    Spec = './Assignments/ITBM01-LIT-00-ZZ-SP-S-001-A1-P01.tex'
    HomeDir = './ITBM01/'
    Archive = 'ITBM01-LIT-00-ZZ-IE-S-001-A1-P01.zip'
    Dwg1Out = 'ITBM01/ITBM01-S-101-A1-.pdf'
    Dwg1 = 'ITBM01-LIT-00-ZZ-DR-S-101-A1-P01.pdf'
}

$Assignment2 = [PSCustomObject]@{
    Name = 'ITBM02-LIT-00-ZZ-SP-S-001-A1-P01'
    Spec = './Assignments/ITBM02-LIT-00-ZZ-SP-S-001-A1-P01.tex'
    HomeDir = './ITBM02/'
    Archive = 'ITBM02-LIT-00-ZZ-IE-S-001-A1-P01.zip'
    Dwg1Out = 'ITBM02/ITBM02-S-101-A1-.pdf'
    Dwg1 = 'ITBM02-LIT-00-ZZ-DR-H-101-A1-P01.pdf'
    Dwg2Out = 'ITBM02/ITBM02-S-102-A1-.pdf'
    Dwg2 = 'ITBM02-LIT-00-ZZ-DR-H-102-A1-P01.pdf'
    Dwg3Out = 'ITBM02/ITBM02-S-103-A1-.pdf'
    Dwg3 = 'ITBM02-LIT-00-ZZ-DR-H-103-A1-P01.pdf'
    Dwg4Out = 'ITBM02/ITBM02-S-104-A1-.pdf'
    Dwg4 = 'ITBM02-LIT-00-ZZ-DR-H-104-A1-P01.pdf'

}

$Assignment3 = [PSCustomObject]@{
    Name = 'ITBM03-LIT-00-ZZ-SP-S-001-A1-P01'
    Spec = './Assignments/ITBM03-LIT-00-ZZ-SP-S-001-A1-P01.tex'
    HomeDir = './ITBM03/'
    Archive = 'ITBM03-LIT-00-ZZ-IE-S-001-A1-P01.zip'
    Dwg1Out = 'ITBM03/ITBM03-M-101-A1-.pdf'
    Dwg1 = 'ITBM03-LIT-00-ZZ-DR-S-101-A1-P01.pdf'
    Dwg2Out = 'ITBM03/ITBM03-S-103-A1-.pdf'
    Dwg2 = 'ITBM03-LIT-00-ZZ-DR-S-103-A1-P01.pdf'
    Dwg3Out = 'ITBM03/ITBM03-M-103-A1-.pdf'
    Dwg3 = 'ITBM03-LIT-00-ZZ-DR-S-103-A1-P01.pdf'
}

$AssetLocation = './Assets/'
$Sheet = 'LIT-A1-Metric-ICBM.rfa'
$ArchModel = 'ITBM01-LIT-00-ZZ-M3-A-001-A1-P01.rvt'




# Cleanout folders
Remove-Item ($Assignment1.HomeDir + '*.*')
Remove-Item ($Assignment2.HomeDir + '*.*')
Remove-Item ($Assignment3.HomeDir + '*.*')
Write-Host 'HomeDir Cleanout'

# Copy Items to Pack Folders

Copy-Item ($AssetLocation + $Sheet) ($Assignment1.HomeDir + $Sheet) -Force
Copy-Item ($AssetLocation + $Sheet) ($Assignment2.HomeDir + $Sheet) -Force
Copy-Item ($AssetLocation + $Sheet) ($Assignment3.HomeDir + $Sheet) -Force
Write-Host 'A1 Sheet Copied to Packs'

#
#Copy-Item ($AssetLocation + $ArchModel) ($Assignment1.HomeDir + $ArchModel) -Force
#Copy-Item ($AssetLocation + $ArchModel) ($Assignment2.HomeDir + $ArchModel) -Force
#Copy-Item ($AssetLocation + $ArchModel) ($Assignment3.HomeDir + $ArchModel) -Force
#Write-Host 'Arch Model Copied to Packs'
#
#Copy-Item ($AssetLocation + $Assignment1.Dwg1Out) ($Assignment1.HomeDir + $Assignment1.Dwg1) -Force
#Write-Host 'ITBM01 Drawings Copied'
#
#
#Copy-Item ($AssetLocation + $Assignment2.Dwg1Out) ($Assignment2.HomeDir + $Assignment2.Dwg1) -Force
#Copy-Item ($AssetLocation + $Assignment2.Dwg2Out) ($Assignment2.HomeDir + $Assignment2.Dwg2) -Force
#Copy-Item ($AssetLocation + $Assignment2.Dwg3Out) ($Assignment2.HomeDir + $Assignment2.Dwg3) -Force
#Write-Host 'ITBM02 Drawings Copied'
#
#
#Copy-Item ($AssetLocation + $Assignment3.Dwg1Out) ($Assignment3.HomeDir + $Assignment3.Dwg1) -Force
#Copy-Item ($AssetLocation + $Assignment3.Dwg2Out) ($Assignment3.HomeDir + $Assignment3.Dwg2) -Force
#Copy-Item ($AssetLocation + $Assignment3.Dwg3Out) ($Assignment3.HomeDir + $Assignment3.Dwg3) -Force
#Write-Host 'ITBM03 Drawings Copied'



# Compile Latex Files


pdflatex $Assignment1.Spec
Remove-Item ($Assignment1.Name + '.aux')
Remove-Item ($Assignment1.Name + '.log')
Remove-Item ($Assignment1.Name + '.out')
Move-Item -Path ($Assignment1.Name + '.pdf') -Destination ($Assignment1.HomeDir + $Assignment1.Name + '.pdf') -Force

pdflatex $Assignment2.Spec
Remove-Item ($Assignment2.Name + '.aux')
Remove-Item ($Assignment2.Name + '.log')
Remove-Item ($Assignment2.Name + '.out')
Move-Item -Path ($Assignment2.Name + '.pdf') -Destination ($Assignment2.HomeDir + $Assignment2.Name + '.pdf') -Force


pdflatex $Assignment3.Spec
Remove-Item ($Assignment3.Name + '.aux')
Remove-Item ($Assignment3.Name + '.log')
Remove-Item ($Assignment3.Name + '.out')
Move-Item -Path ($Assignment3.Name + '.pdf') -Destination ($Assignment3.HomeDir + $Assignment3.Name + '.pdf') -Force


Remove-Item $Assignment1.Archive
Remove-Item $Assignment2.Archive
Remove-Item $Assignment3.Archive


Compress-Archive $Assignment1.HomeDir $Assignment1.Archive -Update
Compress-Archive $Assignment2.HomeDir $Assignment2.Archive -Update
Compress-Archive $Assignment3.HomeDir $Assignment3.Archive -Update


Write-Host -NoNewLine 'Press any key to continue...';
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');