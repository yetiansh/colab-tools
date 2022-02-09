import argparse
import nbformat as nbf


code = """!git clone https://{TOKEN}@github.com/{USER}/{REPO}.git
!cp -r /content/{REPO}/* /content/
!rm -rf /content/{REPO}"""

def str2bool(s):
    if s == "True" or s == "true" or s == "1":
        return True
    else:
        return False

parser = argparse.ArgumentParser()
parser.add_argument("--user", type=str, required=True,
                    help="Your github user name")
parser.add_argument("--repo", type=str, required=True,
                    help="Your github repository name")
parser.add_argument("--token", type=str, required=True, default="",
                    help="Your personal access token")
parser.add_argument("--path", type=str, default="init.ipynb",
                    help="Path to create your repository")

def main(args):
    format_map = {
        "TOKEN": args.token,
        "USER": args.user,
        "REPO": args.repo
    }
    nb = nbf.v4.new_notebook()
    nb["cells"] = [nbf.v4.new_code_cell(code.format_map(format_map))]
    nbf.write(nb, args.path)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
