import os
import subprocess
import boto3


def lambda_handler(event, context):
    # If there is no "package_name", just return with error.
    if "packages_name" in event:
        packages_name = event['packages_name']
    else:
        raise Exception('There is no packages name.')

    # If there is no "s3_bucket_name", just return with error.
    if "s3_bucket_name" in event:
        s3_bucket_name = event['s3_bucket_name']
    else:
        raise Exception('There is no S3 bucket name.')

    # If there is no "s3_path", just make s3_path to blank.
    if "s3_path" in event:
        s3_path = event['s3_path']
    else:
        s3_path = ""

    # If there is no "file_name", just use default file name.
    if "file_name" in event:
        file_name = event['file_name']
    else:
        file_name = "aws-linux-pip-packages.tar"

    # Set subprocess path to tmp.
    os.chdir('/tmp')

    # Make 'packages' directory.
    subprocess.run('mkdir packages'.split())

    # Make pip scripts with package name.
    pip_run_scripts = "pip install".split()
    for x in packages_name:
        pip_run_scripts.append(str(x))
    pip_run_scripts.append("-t")
    pip_run_scripts.append("/tmp/packages")

    # Run pip scripts.
    subprocess.run(pip_run_scripts)

    # Make tar file and upload to S3.
    subprocess.run(('tar -cf %s -C /tmp/packages .' % (file_name, )).split())
    s3 = boto3.client('s3')

    # if s3_path doesn't has backslash, add backslash.
    if s3_path != "" and s3_path[-1:] != "/":
        s3_path = s3_path + "/"

    # if s3_path has backslash in front, remove backslash.
    if s3_path != "" and s3_path[0:1] != "/":
        s3_path = s3_path[1:]

    s3_file_name = s3_path + file_name
    s3.upload_file(file_name, s3_bucket_name, s3_file_name)

    return 'AWS Linux Python package was uploaded successfully.'
