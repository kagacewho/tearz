input_data = open('input.txt', 'r') 
data = input_data.read()
S = int(data)
out = str(int(S/6)) + " " + str(int(4 * S/6)) + " " + str(int(S/6))
output_data = open('output.txt', 'w')
output_data.write(str(out))
input_data.close()
output_data.close()
https://yandex.ru/q/question/kak_postroit_parabolu_v_python_cc888cad/
