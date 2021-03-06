import argparse
import NoiseMain as PN

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--size', '-s', metavar='s', type=int, required=True, help='The size of the noise image')
parser.add_argument('--iteration', '-d', metavar='d', type=int, required=True, help='Iterations for the smoothing')
parser.add_argument('--height', metavar='h', type=int, required=False, help='Size of the ellipse/rectangle')
parser.add_argument('--HE', metavar='he', type=float, required=False, help="Roughness. Use small values")
parser.add_argument('--SP', metavar='sp', type=float, required=False, help="Spread. Size of the generated spots")
parser.add_argument('-e', '--ellipse', action='store_true', required=False, help='Uses Ellipse drawer')
parser.add_argument('-r', '--rectangle', action='store_true', required=False, help='Uses Rectangle drawer')
parser.add_argument('-p', '--pie', action='store_true', required=False, help='Uses Pie drawer')
parser.add_argument('--seed', type=int, required=False, help='Seed Value for the random number generator')
parser.add_argument('--name', '-n', metavar='n', type=str, required=True, help='The name of the noise')

args = parser.parse_args()

size = args.size
iteration = args.iteration
height = args.height
he = args.HE
name = args.name
sp = args.SP

if not he:
    he = 0.0
if not sp:
    sp = 0.0

noise1 = PN.Noise(size, iteration, sp, he, 255)

if args.seed:
    noise1.seed(args.seed)
noise1.generate()

if args.ellipse:
    if height:
        noise1.generateEllipse(height)
    else:
        raise (Exception("height is required"))

if args.rectangle:
    if height:
        noise1.generateRect(height)
    else:
        raise(Exception("height is required"))

if args.pie:
    if height:
        noise1.generatePie(height)
    else:
        raise(Exception("height is required"))

noise1.smooth()
noise1.save("", name)
