import os
import tomllib

import toml
from absl import app, flags

import lib

flags.DEFINE_string(
    "dois",
    None,
    "Path to the dois.toml containing the list of article DOIs to filter for open access-only articles.",
)
flags.DEFINE_string(
    "email",
    None,
    "Email to access Unpaywall API for determining open access status of article.",
)
flags.DEFINE_string("out", None, "Path to write the open access DOIs.")

flags.mark_flag_as_required("dois")
flags.mark_flag_as_required("email")
flags.mark_flag_as_required("out")


def main(argv: list[str]) -> None:
    if len(argv) > 1:
        raise ValueError("too many positional arguments")
    del argv

    os.environ["UNPAYWALL_EMAIL"] = flags.FLAGS.email
    with open(flags.FLAGS.dois, "rb") as f:
        dois = tomllib.load(f)
    with open(flags.FLAGS.out, "w") as f:
        toml.dump({"dois": lib.access(dois["dois"])}, f)


if __name__ == "__main__":
    app.run(main)
