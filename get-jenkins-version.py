import requests

def get_revision_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('cannot connect on url {}'.format(url)) 
    json = response.json()
    for b in json['builds']:
        if b['result'] != 'SUCCESS':
            continue
        branch = b['actions'][0]['parameters'][0]['value']
        if not 'Arg' in branch:
            continue
        if len(b['changeSets']) <= 0:
            continue
        build_number = b['number']
        revision = b['changeSets'][0]['items'][0]['revision']
        return 'r{}_b{}'.format(revision, build_number)

def get_file(nexus_url, jenkins_url, file_name):
    revision = get_revision_url(jenkins_url)
    file_url = '{}{}/Deploy-{}-dev.zip'.format(nexus_url, revision, revision)
    response = requests.get(file_url)
    if response.status_code != 200:
        raise Exception('cannot download file on url {}'.format(file_url)) 
    with open(file_name, 'wb') as f:
        f.write(response.content)

job = 'ACS-CSOnline-Dev'
branch = 'Arg-Sprint'
file_name = 'csonline.zip'
nexus_url = 'https://nexus.minhati.com.br/repository/raw/com/raizen/acs/csonline/Deploy/'
jenkins_url = 'https://jenkins.minhati.com.br/view/CSOnline/job/{}/api/json?tree=builds[actions[parameters[name,value]],number,status,id,result,changeSets[items[revision,RepositoryUrl]]]'.format(job)
get_file(nexus_url, jenkins_url, file_name)
