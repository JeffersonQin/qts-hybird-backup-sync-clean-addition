import datetime
import click
import os


@click.group()
def cli():
    pass


@cli.command()
@click.argument("path", type=click.Path(exists=True))
def clean(path: click.Path):
	"""Clean redundant syncing storage

	Args:
		path (click.Path): Path to clean
	"""
	g = os.walk(path)
	for path, dir_list, file_list in g:
		for file_name in file_list:
			file_name_base = os.path.splitext(file_name)[0]
			file_name_extension = os.path.splitext(file_name)[-1]
			for check_file_name in file_list:
				if check_file_name == file_name: continue

				check_file_name_base = os.path.splitext(check_file_name)[0]
				check_file_name_extension = os.path.splitext(check_file_name)[-1]
				
				if check_file_name_extension != file_name_extension or \
					not check_file_name_base.startswith(file_name_base):
					continue

				time_format_str = check_file_name_base[len(file_name_base):]
				
				delete = False

				try:
					_ = datetime.datetime.strptime(time_format_str, ' - %Y-%m-%dT%H%M%S.%fZ')
					delete = True
				except: pass

				if delete:
					file_path = os.path.join(path, check_file_name)
					os.remove(file_path)
					print("Delete file:", file_path)


if __name__ == '__main__':
    cli()
