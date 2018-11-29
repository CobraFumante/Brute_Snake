class welcome():
    def __init__(self):
        self.choose = ''
        self.available = ['1']
    def hello(self):
        print('\n'
              '           /^\\/^\\ \n'
              '          |O__|  O|\n'
              '\\/     /~     \_/ \\\n'
              ' \\____|__________/  \\\n'
              '        \_______      \\\n'
              '                `\\     \\                 \\\n'
              '                  |     |                  \\\n'
              '                 /      /                    \\\n'
              '                /     /                       \\\\\n'
              '              /      /                         \\ \\\n'
              '             /     /                            \\  \\\n'
              '           /     /             _----_            \\   \\\n'
              '          /     /           _-~      ~-_         |   |\n'
              '         (      (        _-~    _--_    ~-_     _/   |\n'
              '          \\      ~-____-~    _-~    ~-_    ~-_-~    /\n'
              '            ~-_           _-~          ~-_       _-~\n'
              '               ~--______-~                ~-___-~\n'
              '\n'
              '\n')
        self.choose = input('Qual módulo deseja escolher? - Why module do you want?\n'
                            '[1]pdf_snake\n')
        while self.choose not in self.available:
            self.choose = input('Qual módulo deseja escolher? - Which module do you want?\n'
                            '[1]pdf_snake\n')
    def run(self):
        if self.choose == '1':
            import sys
            import pdf_snake
            pdf = pdf_snake
            pdf.Pdf_snake().GetLocate()
            pdf.Pdf_snake().GetMode()
            pdf.Pdf_snake().DefineList()
            pdf.Pdf_snake().DoIt()

wel = welcome()
wel.hello()
wel.run()
