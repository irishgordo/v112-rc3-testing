import os

def main():
    pictures = os.listdir()
    try:
        os.remove('README.md')
        print(f'removed old readme')
    except OSError as ex:
        pass
    with open("README.md", "w") as readme:
        for pic in pictures:
            if pic != 'write_dir_files_to_markdown.py' and pic != 'README.md':
                readme.write('\n')
                sntzepic = pic.replace(' ', '\\ ')
                mrkdwnpic = (f'![{pic}]({sntzepic})')
                readme.write(mrkdwnpic)
                readme.write('\n')

if __name__ == "__main__":
    main()
