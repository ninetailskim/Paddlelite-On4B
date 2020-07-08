from paddlelite.lite import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--md', type=str, default=None)
parser.add_argument('--mf', type=str)
parser.add_argument('--hf', type=str)
parser.add_argument('--vp', type=str, default='arm')
parser.add_argument('--mt', type=str, default='naive_buffer')
parser.add_argument('--oo', type=str, default='opttest')

args = parser.parse_args()

opt = Opt()

if args.md is not None:
    opt.set_model_dir(args.md)
    print("md")
else:
    opt.set_model_file(args.mf)
    opt.set_param_file(args.hf)
    print("mf&hf")

opt.set_valid_places(args.vp)
opt.set_model_type(args.mt)
opt.set_optimize_out(args.oo)
print("start run")
opt.run()