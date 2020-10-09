import conducto as co


def pr(branch=None) -> co.Parallel:
    image = co.Image("python:alpine", copy_repo=True, copy_branch=branch)
    with co.Parallel(image=image) as root:
        co.Exec(f"echo {branch}", name="print branch")
        co.Exec("pwd", name="print working directory")
        co.Exec("ls -la", name="list files")
    return root


if __name__ == "__main__":
    co.main()
