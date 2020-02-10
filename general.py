import os



# Each website is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'     # list of links waiting to be crawled
    crawled = project_name + '/crawled.txt'     # list of links already crawled
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data to existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete content of file
def delete_file_content(path):
    open(path, 'w').close()


# Read from file to list
def file_to_set(file_name):
    result = set()
    with open(file_name, 'rt') as f:
        #result.add(f.readline().replace('\n', ''))
        for line in f:
            result.add(line.replace('\n', ''))
        #result = {line.replace('\n','') for line in f}
    return result


# Iterate through set
def set_to_file(links, file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file, link)


