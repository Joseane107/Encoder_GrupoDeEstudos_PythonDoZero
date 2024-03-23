## vamos criar um codificador de texto onde o programa
## recebe um texto e retorna o texto codificado     

#vamos usar a biblioteca base64 para codificar o texto
                   
class first_encoder:
    def __init__(self):
        pass

    def get_message(self):
        self.message = input('Type a message:  ')

        letters = []
        for i in range(0, len(self.message)):
            letters.append(self.message[i])
        print(letters)

    def convert_to_bytes(self):
        self.get_message()
        msg_to_bytes = bytes(self.message, 'utf-8')

        self.bytes_list = []

        for i in msg_to_bytes:
            self.bytes_list.append(i)
        print(self.bytes_list)

    def bytes_to_bit(self):
        self.convert_to_bytes()

        self.bit_list = []
        for i in self.bytes_list:
            self.bit_list.append(format(i, 'b'))
        print(self.bit_list)

    def binary_together(self):
        self.bytes_to_bit()

        self.bin = ''
        for i in self.bit_list:
            self.bin = self.bin + i
        print(self.bin)

    def set_to_6_bits(self):
        self.binary_together()

        length = len(self.bin)
        print(length)
        div = int(length/6)

        self.six_bits_list = []

        j = 0
        for i in range (1,div + 1):
            self.six_bits_list.append(self.bin[j:6*i])
            j = 6*i 
        print(self.six_bits_list)
