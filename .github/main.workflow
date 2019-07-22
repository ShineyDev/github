workflow "Test and upload on tag" {
  on = "push"
  resolves = ["Twine upload"]
}

action "Filter tag" {
  uses = "actions/bin/filter@master"
  args = "tag"
}

action "Test 3.5" {
  uses = "orangutangaming/actions/pytest-install-35@master"
  needs = ["Filter tag"]
}

action "Test 3.6" {
  uses = "orangutangaming/actions/pytest-install-36@master"
  needs = ["Filter tag"]
}

action "Test 3.7" {
  uses = "orangutangaming/actions/pytest-install-37@master"
  needs = ["Filter tag"]
}

action "Twine upload" {
  uses = "orangutangaming/actions/twine-upload@master"
  secrets = ["TWINE_PASSWORD"]
  needs = ["Test 3.5", "Test 3.6", "Test 3.7"]
  env = {
    TWINE_USERNAME = "ShineyDev"
  }
}
