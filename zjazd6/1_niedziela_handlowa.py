import argparse


parser.add_argument('filename')
parser.add_argument('-m', '--mode', default='m')
parser.add_argument('-ex', '--extension', default='txt')

args = parser.parse_args()

print(f'Nazwa pliku to: {args.filename}')
print(f'Tryb to: {args.mode}')
print(f'Rozszerzenie to: {args.extension}')

file = args.filename + '.' + args.extension
print(file)

with open(args.filename, 'r') as file1:
    content = file1.read()

print(content)