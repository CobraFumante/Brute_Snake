class Pdf_snake():
    def __init__(self):
        import PyPDF2
        import os
        self.BruteForceCaracteresList = []
        self.BruteForceCreatedList = []
        self.osmodule = os
        self.nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.alphalower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                           't', 'u', 'v', 'w', 'x', 'y', 'z', ]

        self.alphaupper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                           'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]
        self.ChooseMode = ''
        self.NumberOfCaracteres = ''
        self.Caracteres = ''
        self.BruteForceListLocate = ''
        self.BruteForceList = ''
        self.finded = False

    def GetLocate(self):
        import PyPDF2
        self.locate = input('Digite o local onde o arquivo pdf se encontra - Insert the path where the pdf file is  ')
        while self.osmodule.path.exists(self.locate) is not True or self.locate[-4:] != '.pdf':
            print('Diretório Invalido, Digite novamente - invalid directory, insert it again')
            self.locate = input('Digite o local onde o arquivo pdf se encontra - Insert the path where the pdf file is  ')
        self.pdffilereader = PyPDF2.PdfFileReader(self.locate)

    def GetMode(self):
        self.ChooseMode = str(input('\n'
                  'escolha o modo - Choose de mode:\n'
                  '1 = [Brute Force]\n'
                  '2 = [list BruteFoce]\n'))
        if self.ChooseMode == '1':
            self.NumberOfCaracteres = input('Quantos caracteres deseja - how many caracteres do you wish?')
            self.Caracteres = int(input('\n'
                                        'Digite o numero dos caracteres que deseja colocar no brute force - insert the '
                                        'number of the caracteres tha you want to put in the brute force\n'
                                        '[1]Nums\n'
                                        '[2]alphalower\n'
                                        '[3]alphaupper'))
        else:
            self.BruteForceListLocate = input('Onde está a lista de brute force? - wheres the brute force list? ')
            while self.osmodule.path.exists(self.BruteForceListLocate) is not True or self.BruteForceListLocate[-4:] != '.txt':
                print('Diretório Invalido, Digite novamente - invalid directory, insert it again')
                self.BruteForceListLocate = input('Onde está a lista de brute force? - wheres the brute force list? ')

    def CreateList(self):
        for atual in range(int(self.NumberOfCaracteres)):
            a = [i for i in self.BruteForceCaracteresList]
            for y in range(atual):
                a = [x + i for i in self.BruteForceCaracteresList for x in a]
            self.BruteForceCreatedList = self.BruteForceCreatedList + a

    def DefineList(self):
        if self.ChooseMode == '1':
            for a in str(self.Caracteres):
                if a == '1':
                    for x in self.nums:
                        self.BruteForceCaracteresList.append(x)
                if a == '2':
                    for y in self.alphalower:
                        self.BruteForceCaracteresList.append(y)
                if a == '3':
                    for z in self.alphaupper:
                        self.BruteForceCaracteresList.append(z)
            self.CreateList()
        if self.ChooseMode == '2':
            self.BruteForceList = open(self.BruteForceListLocate, 'r')
            self.BruteForceCreatedList = self.BruteForceList.read().split()
            print(self.BruteForceCreatedList)

    def DoIt(self):
        import sys
        for i in self.BruteForceCreatedList:
            if self.pdffilereader.decrypt(i) == 1:
                print(f'[+]Senha Encontrada : {i}')
                self.finded = True
                break
            else:
                print(f'[-]Senha Falhou : {i}')
        if self.finded == True:
            print('Parabéns, A cobra Fumou - Congratulations, The Snake haved a green day {:')
        else:
            print('Senha não encontrada - Password Didnt Find')
