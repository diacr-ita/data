import sys
import os


def main(folder_in, folder_out, mode):
    for f_name in os.listdir(folder_in):
        with open(os.path.join(folder_in,f_name),"r") as f:
             with open(os.path.join(folder_out,f_name),'w+') as g: 
                  newline=[]
                  for line in f:
                      if line=='\n':
                         g.write(' '.join(newline)+'\n')
                         newline=[]
                      else:
                         if mode==0:
                            tok=line.split()[0]
                         elif mode==1:
                            tok=line.split()[2]
                         elif mode==2:
                            line=line.split()
                            tok=line[0]+'_'+line[1]
                         else:
                            line=line.split()
                            tok=line[2]+'_'+line[1]
                         newline.append(tok)



if __name__ == "__main__":
    args = sys.argv
    if not len(args)==4:
       print('Missing arguments')
       exit()
    folder_in = args[1]
    folder_out = args[2]
    mode = int(args[3])
    if not os.path.exists(folder_in):
       print('Folder input doesn\'t exits.')
       exit()
    if not os.path.exists(folder_out):
       print('Folder output doesn\'t exits.')
       exit()
    if not (mode>=0 and mode<=3):
       print('Select one of those:')
       print('0 Raw text')
       print('1 Lemma')
       print('2 Raw text + PoS Tag')
       print('3 Lemma + PoS Tag')
       exit()
    main(folder_in,folder_out,mode)
