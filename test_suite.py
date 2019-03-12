from selenium import webdriver
import unittest
import time
import pdb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_gluster_deployment_fail_check():
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True

    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('https://10.70.42.231:9090')

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, "login-user-input")))
    loginUserInput = driver.find_element_by_id("login-user-input")
    loginUserInput.send_keys("root")
    loginPasswordInput = driver.find_element_by_id("login-password-input")
    loginPasswordInput.send_keys("redhat")
    loginButton = driver.find_element_by_id("login-button")
    loginButton.click()

    time.sleep(15)
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Virtualization")))
    driver.switch_to_frame(1)
    HostedEngine = driver.find_element_by_link_text("Hosted Engine")
    assert HostedEngine.text == "Hosted Engine"
    HostedEngine.click()

    time.sleep(5)
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.url_changes("https://10.70.42.231:9090/ovirt-dashboard#/he"))
    GlusterWizard = driver.find_element_by_xpath("//div[@id='content']/div/div/div/div/div/div[3]/span[2]/button")
    assert GlusterWizard.text == "Start"
    GlusterWizard.click()

    ThreeNodeDep = driver.find_element_by_css_selector(".col-sm-3 > .btn")
    assert ThreeNodeDep.text == "Run Gluster Wizard"
    ThreeNodeDep.click()

    driver.find_element_by_css_selector(".form-horizontal:nth-child(1) > div:nth-child(1) > .form-group .form-control").send_keys("h")
    driver.find_element_by_css_selector(".form-horizontal:nth-child(1) > div:nth-child(2) > .form-group .form-control").send_keys("hh")
    driver.find_element_by_css_selector("div:nth-child(3) > .form-group .form-control").send_keys("hhh")

    driver.find_element_by_css_selector(".wizard-pf-next").click()

    fqdnAssert = driver.find_element_by_css_selector(".form-horizontal > .col-md-offset-2")
    assert fqdnAssert.text == "Provide the address used to add the additional hosts to be managed by Hosted Engine preferrably FQDN or IP address. And both FQDN needs to be added in known_hosts file."
    driver.find_element_by_css_selector(".wizard-pf-next").click()

    packageAssert = driver.find_element_by_css_selector(".form-horizontal > .form-group:nth-child(2) > .col-md-2:nth-child(1)")
    assert packageAssert.text == "Packages"
    driver.find_element_by_css_selector(".wizard-pf-next").click()

    AddVolume = driver.find_element_by_css_selector("strong:nth-child(1)")
    assert AddVolume.text == "Add Volume"
    AddVolume.click()
    EmptyVolumeName = driver.find_element_by_css_selector("tr:nth-child(5) > .col-md-3:nth-child(1) .form-control")
    EmptyVolumeName.send_keys("testvol")
    driver.find_element_by_css_selector(".wizard-pf-next").click()

    RaidInformationTitle = driver.find_element_by_css_selector(".form-horizontal > .panel-heading > .panel-title")
    assert RaidInformationTitle.text == "Raid Information"
    RaidTypeDropDown = driver.find_element_by_css_selector(".col-md-2 .btn")
    assert RaidTypeDropDown.text == "RAID 6"
    RaidTypeDropDown.click()
    driver.find_element_by_link_text("JBOD").click()
    assert RaidTypeDropDown.text == "JBOD"
    driver.find_element_by_css_selector(".wizard-pf-next").click()

    ansibleConfig = driver.find_element_by_css_selector(".ansible-wizard-config-preview")
    print ansibleConfig.text
    DeploymentMsg = driver.find_element_by_css_selector("div:nth-child(1) > span:nth-child(2)")
    assert DeploymentMsg.text == "Generated Ansible inventory : /etc/ansible/hc_wizard_inventory.yml"

    driver.find_element_by_css_selector(".wizard-pf-finish").click()

    spinner = driver.find_element_by_css_selector(".spinner")
    try:
        while spinner.is_displayed():
            print "check: ", spinner.text
    except:
        print "Element not visible"

    DeploymentMsg = driver.find_element_by_css_selector("div:nth-child(1) > span:nth-child(2)")
    assert DeploymentMsg.text == "Deployment failed"

    driver.close()
    driver.quit()

def test_gluster_empty_host_validation_check():
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True

    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('https://10.70.42.231:9090')

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, "login-user-input")))
    loginUserInput = driver.find_element_by_id("login-user-input")
    loginUserInput.send_keys("root")
    loginPasswordInput = driver.find_element_by_id("login-password-input")
    loginPasswordInput.send_keys("redhat")
    loginButton = driver.find_element_by_id("login-button")
    loginButton.click()

    time.sleep(15)
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Virtualization")))
    driver.switch_to_frame(1)
    HostedEngine = driver.find_element_by_link_text("Hosted Engine")
    assert HostedEngine.text == "Hosted Engine"
    HostedEngine.click()

    time.sleep(5)
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.url_changes("https://10.70.42.231:9090/ovirt-dashboard#/he"))
    GlusterWizard = driver.find_element_by_xpath("//div[@id='content']/div/div/div/div/div/div[3]/span[2]/button")
    assert GlusterWizard.text == "Start"
    GlusterWizard.click()

    ThreeNodeDep = driver.find_element_by_css_selector(".col-sm-3 > .btn")
    assert ThreeNodeDep.text == "Run Gluster Wizard"
    ThreeNodeDep.click()

    driver.find_element_by_css_selector(".wizard-pf-next").click()

    host1 = driver.find_element_by_css_selector("div:nth-child(1) > .form-group .help-block")
    host2 = driver.find_element_by_css_selector("div:nth-child(2) > .form-group .help-block")
    host3 = driver.find_element_by_css_selector("div:nth-child(3) > .form-group .help-block")

    assert host1.text == "Host address cannot be empty"
    assert host2.text == "Host address cannot be empty"
    assert host3.text == "Host address cannot be empty"

    driver.close()
    driver.quit()

def test_gluster_fqdn_validation_check():
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True

    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('https://10.70.42.231:9090')

    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.visibility_of_element_located((By.ID, "login-user-input")))
    loginUserInput = driver.find_element_by_id("login-user-input")
    loginUserInput.send_keys("root")
    loginPasswordInput = driver.find_element_by_id("login-password-input")
    loginPasswordInput.send_keys("redhat")
    loginButton = driver.find_element_by_id("login-button")
    loginButton.click()

    time.sleep(15)
    # wait = WebDriverWait(driver, 15)
    # element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Virtualization")))
    driver.switch_to_frame(1)
    HostedEngine = driver.find_element_by_link_text("Hosted Engine")
    assert HostedEngine.text == "Hosted Engine"
    HostedEngine.click()

    time.sleep(5)
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.url_changes("https://10.70.42.231:9090/ovirt-dashboard#/he"))
    GlusterWizard = driver.find_element_by_xpath("//div[@id='content']/div/div/div/div/div/div[3]/span[2]/button")
    assert GlusterWizard.text == "Start"
    GlusterWizard.click()

    ThreeNodeDep = driver.find_element_by_css_selector(".col-sm-3 > .btn")
    assert ThreeNodeDep.text == "Run Gluster Wizard"
    ThreeNodeDep.click()

    driver.find_element_by_css_selector(".form-horizontal:nth-child(1) > div:nth-child(1) > .form-group .form-control").send_keys("h")
    driver.find_element_by_css_selector(".form-horizontal:nth-child(1) > div:nth-child(2) > .form-group .form-control").send_keys("hh")
    driver.find_element_by_css_selector("div:nth-child(3) > .form-group .form-control").send_keys("hhh")

    driver.find_element_by_css_selector(".wizard-pf-next").click()

    handleSameFqdnAsHost = driver.find_element_by_id("handleSameFqdnAsHost")
    handleSameFqdnAsHost.click()

    fqdn1_Error = driver.find_element_by_css_selector("div:nth-child(1) > .form-group .help-block")
    fqdn2_Error = driver.find_element_by_css_selector("div:nth-child(2) > .form-group .help-block")

    assert fqdn1_Error.text == "Host is not reachable"
    assert fqdn2_Error.text == "Host is not reachable"

    handleSameFqdnAsHost.click()
    time.sleep(1)

    fqdn1_textArea = driver.find_element_by_id("fqdn")
    fqdn2_textArea = driver.find_element_by_css_selector("div:nth-child(2) > .form-group #fqdn")

    fqdn1_textArea.send_keys("10.70.42.231")
    fqdn2_textArea.send_keys("10.70.42.231")

    driver.find_element_by_css_selector(".wizard-pf-next").click()

    fqdnSameError = driver.find_element_by_css_selector(".col-md-6 > .help-block")
    assert fqdnSameError.text == "Both fqdn or ip can not be same."

    fqdn2_textArea.clear()

    driver.find_element_by_css_selector(".wizard-pf-next").click()

    fqdnEmptyError = driver.find_element_by_css_selector(".col-md-6 > .help-block")
    assert fqdnEmptyError.text == "Please provide fqdn or ip for both hosts."

    driver.close()
    driver.quit()

def test_gluster_volume_validation_check():
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True

    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('https://10.70.42.231:9090')

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, "login-user-input")))
    loginUserInput = driver.find_element_by_id("login-user-input")
    loginUserInput.send_keys("root")
    loginPasswordInput = driver.find_element_by_id("login-password-input")
    loginPasswordInput.send_keys("redhat")
    loginButton = driver.find_element_by_id("login-button")
    loginButton.click()

    time.sleep(15)
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Virtualization")))
    driver.switch_to_frame(1)
    HostedEngine = driver.find_element_by_link_text("Hosted Engine")
    assert HostedEngine.text == "Hosted Engine"
    HostedEngine.click()

    time.sleep(5)
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.url_changes("https://10.70.42.231:9090/ovirt-dashboard#/he"))
    GlusterWizard = driver.find_element_by_xpath("//div[@id='content']/div/div/div/div/div/div[3]/span[2]/button")
    assert GlusterWizard.text == "Start"
    GlusterWizard.click()

    ThreeNodeDep = driver.find_element_by_css_selector(".col-sm-3 > .btn")
    assert ThreeNodeDep.text == "Run Gluster Wizard"
    ThreeNodeDep.click()

    driver.find_element_by_css_selector(".form-horizontal:nth-child(1) > div:nth-child(1) > .form-group .form-control").send_keys("h")
    driver.find_element_by_css_selector(".form-horizontal:nth-child(1) > div:nth-child(2) > .form-group .form-control").send_keys("hh")
    driver.find_element_by_css_selector("div:nth-child(3) > .form-group .form-control").send_keys("hhh")

    driver.find_element_by_css_selector(".wizard-pf-next").click()

    fqdnAssert = driver.find_element_by_css_selector(".form-horizontal > .col-md-offset-2")
    assert fqdnAssert.text == "Provide the address used to add the additional hosts to be managed by Hosted Engine preferrably FQDN or IP address. And both FQDN needs to be added in known_hosts file."
    driver.find_element_by_css_selector(".wizard-pf-next").click()

    packageAssert = driver.find_element_by_css_selector(".form-horizontal > .form-group:nth-child(2) > .col-md-2:nth-child(1)")
    assert packageAssert.text == "Packages"
    driver.find_element_by_css_selector(".wizard-pf-next").click()

    AddVolume = driver.find_element_by_css_selector("strong:nth-child(1)")
    assert AddVolume.text == "Add Volume"
    AddVolume.click()

    driver.find_element_by_css_selector(".wizard-pf-next").click()

    assert driver.find_element_by_css_selector(".col-md-3:nth-child(1) .help-block").text == "Volume name cannot be empty"
    assert driver.find_element_by_css_selector(".col-md-3:nth-child(4) .help-block").text == "Brick directory cannot be empty"

    driver.find_element_by_css_selector("tr:nth-child(5) .pficon").click()

    driver.find_element_by_css_selector(".wizard-pf-next").click()

    RaidInformationTitle = driver.find_element_by_css_selector(".form-horizontal > .panel-heading > .panel-title")
    assert RaidInformationTitle.text == "Raid Information"

    driver.close()
    driver.quit()

def test_gluster_vdo_present():
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True

    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('https://10.70.42.231:9090')

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, "login-user-input")))
    loginUserInput = driver.find_element_by_id("login-user-input")
    loginUserInput.send_keys("root")
    loginPasswordInput = driver.find_element_by_id("login-password-input")
    loginPasswordInput.send_keys("redhat")
    loginButton = driver.find_element_by_id("login-button")
    loginButton.click()

    time.sleep(15)
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Virtualization")))
    driver.switch_to_frame(1)
    HostedEngine = driver.find_element_by_link_text("Hosted Engine")
    assert HostedEngine.text == "Hosted Engine"
    HostedEngine.click()

    time.sleep(5)
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.url_changes("https://10.70.42.231:9090/ovirt-dashboard#/he"))
    GlusterWizard = driver.find_element_by_xpath("//div[@id='content']/div/div/div/div/div/div[3]/span[2]/button")
    assert GlusterWizard.text == "Start"
    GlusterWizard.click()

    ThreeNodeDep = driver.find_element_by_css_selector(".col-sm-3 > .btn")
    assert ThreeNodeDep.text == "Run Gluster Wizard"
    ThreeNodeDep.click()

    driver.find_element_by_css_selector(".form-horizontal:nth-child(1) > div:nth-child(1) > .form-group .form-control").send_keys("h")
    driver.find_element_by_css_selector(".form-horizontal:nth-child(1) > div:nth-child(2) > .form-group .form-control").send_keys("hh")
    driver.find_element_by_css_selector("div:nth-child(3) > .form-group .form-control").send_keys("hhh")

    driver.find_element_by_css_selector(".wizard-pf-next").click()

    fqdnAssert = driver.find_element_by_css_selector(".form-horizontal > .col-md-offset-2")
    assert fqdnAssert.text == "Provide the address used to add the additional hosts to be managed by Hosted Engine preferrably FQDN or IP address. And both FQDN needs to be added in known_hosts file."
    driver.find_element_by_css_selector(".wizard-pf-next").click()

    packageAssert = driver.find_element_by_css_selector(".form-horizontal > .form-group:nth-child(2) > .col-md-2:nth-child(1)")
    assert packageAssert.text == "Packages"
    driver.find_element_by_css_selector(".wizard-pf-next").click()
    driver.find_element_by_css_selector(".wizard-pf-next").click()

    RaidInformationTitle = driver.find_element_by_css_selector(".form-horizontal > .panel-heading > .panel-title")
    assert RaidInformationTitle.text == "Raid Information"

    try:
        vdocheck = driver.find_element_by_css_selector(".ansible-wizard-bricks-row:nth-child(2) > .col-md-1:nth-child(6) > .ansible-wizard-thinp-checkbox")
        vdocheck.click()

        h1Size = driver.find_element_by_css_selector(".ansible-wizard-bricks-row:nth-child(2) > .col-md-1:nth-child(3) .form-control")
        h1VdoSize = driver.find_element_by_css_selector(".ansible-wizard-bricks-row:nth-child(2) > .col-md-1:nth-child(7) .form-control")
        assert 10*int(h1Size.get_attribute('value')) == int(h1VdoSize.get_attribute('value'))

        h2Size = driver.find_element_by_css_selector(".ansible-wizard-bricks-row:nth-child(3) > .col-md-1:nth-child(3) .form-control")
        h2VdoSize = driver.find_element_by_css_selector(".ansible-wizard-bricks-row:nth-child(3) > .col-md-1:nth-child(7) .form-control")
        assert 10*int(h2Size.get_attribute('value')) == int(h2VdoSize.get_attribute('value'))

        h3Size = driver.find_element_by_css_selector(".ansible-wizard-bricks-row:nth-child(4) > .col-md-1:nth-child(3) .form-control")
        h3VdoSize = driver.find_element_by_css_selector(".ansible-wizard-bricks-row:nth-child(4) > .col-md-1:nth-child(7) .form-control")
        assert 10*int(h3Size.get_attribute('value')) == int(h3VdoSize.get_attribute('value'))

    except:
        print "VDO not present"

    driver.close()
    driver.quit()
