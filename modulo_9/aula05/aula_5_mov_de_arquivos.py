import os
import shutil

os.chdir('modulo_9' + os.sep + 'aula05')
shutil.copy(src='nomes.txt', dst='Arquivos 2010')
shutil.move(src='inscrições.pdf', dst='Documentação')
shutil.make_archive('Documentação', 'zip', 'Documentação')
shutil.move(src='Documentação.zip', dst='Backup')
shutil.rmtree('Arquivos 2010')
shutil.rmtree('Documentação')
os.chdir('..')
shutil.make_archive('Backup Arquivos Python', 'zip', 'aula05')