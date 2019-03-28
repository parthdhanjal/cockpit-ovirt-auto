import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class oVirtDashboardPageObjects():

    URL = "https://10.70.42.231:9090"
    ACCEPT_UNTRUSTED_CERTS = True

    loginUserInput = "login-user-input"
    loginUserInputValue = "root"
    loginPasswordInput = "login-password-input"
    loginPasswordInputValue = "redhat"
    loginButton = "login-button"

    heFrame = 1
    hostedEngineButtonText = "Hosted Engine"

    glusterWizardButton = "//div[@id='content']/div/div/div/div/div/div[3]/span[2]/button"
    glusterWizardButtonText = "Start"

    ThreeNodeDepButton = ".col-sm-3 > .btn"
    ThreeNodeDepButtonText = "Run Gluster Wizard"

    host1Input = ".form-horizontal:nth-child(1) > div:nth-child(1) > .form-group .form-control"
    host1InputValue = "h"
    host1Error = "div:nth-child(1) > .form-group .help-block"

    host2Input = ".form-horizontal:nth-child(1) > div:nth-child(2) > .form-group .form-control"
    host2InputValue = "hh"
    host2Error = "div:nth-child(2) > .form-group .help-block"

    host3Input = "div:nth-child(3) > .form-group .form-control"
    host3InputValue = "hhh"
    host3Error = "div:nth-child(3) > .form-group .help-block"

    hostEmptyErrorValue = "Host address cannot be empty"

    wizardNextButton = ".wizard-pf-next"

    handleSameFqdnAsHost = "handleSameFqdnAsHost"
    fqdnAssertBox = ".form-horizontal > .col-md-offset-2"
    fqdnAssertBoxValue = "Provide the address used to add the additional hosts to be managed by Hosted Engine preferrably FQDN or IP address. And both FQDN needs to be added in known_hosts file."

    validFqdn = "10.70.42.231"

    fqdn1Input = "fqdn"
    fqdn1Error = "div:nth-child(1) > .form-group .help-block"

    fqdn2Input = "div:nth-child(2) > .form-group #fqdn"
    fqdn2Error = "div:nth-child(2) > .form-group .help-block"

    fqdnError = ".col-md-6 > .help-block"
    fqdnSameErrorValue = "Both fqdn or ip can not be same."
    fqdnEmptyError = "Please provide fqdn or ip for both hosts."
    fqdnUnreachableError = "Host is not reachable"

    packageAssertBox = ".form-horizontal > .form-group:nth-child(2) > .col-md-2:nth-child(1)"
    packageAssertBoxValue = "Packages"

    addVolumeButton = "strong:nth-child(1)"
    addVolumeButtonValue = "Add Volume"
    EmptyVolumeName = "tr:nth-child(5) > .col-md-3:nth-child(1) .form-control"
    EmptyVolumeNameText = ''
    EmptyVolumeNameValue = "testvol"
    ErrorVolumeName = ".col-md-3:nth-child(1) .help-block"
    ErrorGlusterBrickDirectory = ".col-md-3:nth-child(4) .help-block"
    ErrorVolumeNameValue = "Volume name cannot be empty"
    ErrorGlusterBrickDirectoryValue = "Brick directory cannot be empty"
    deleteVolumeIcon = "tr:nth-child(5) .pficon"

    RaidInformationTitle = ".form-horizontal > .panel-heading > .panel-title"
    RaidInformationTitleText = "Raid Information"
    RaidTypeDropDown = ".col-md-2 .btn"
    RaidTypeDropDownText = "RAID 6"
    RaidTypeDropDownTextAlter = "JBOD"

    vdoCheckBox = ".ansible-wizard-bricks-row:nth-child(2) > .col-md-1:nth-child(6) > .ansible-wizard-thinp-checkbox"
    h1Size = ".ansible-wizard-bricks-row:nth-child(2) > .col-md-1:nth-child(3) .form-control"
    h1VdoSize = ".ansible-wizard-bricks-row:nth-child(2) > .col-md-1:nth-child(7) .form-control"
    h2Size = ".ansible-wizard-bricks-row:nth-child(3) > .col-md-1:nth-child(3) .form-control"
    h2VdoSize = ".ansible-wizard-bricks-row:nth-child(3) > .col-md-1:nth-child(7) .form-control"
    h3Size = ".ansible-wizard-bricks-row:nth-child(4) > .col-md-1:nth-child(3) .form-control"
    h3VdoSize = ".ansible-wizard-bricks-row:nth-child(4) > .col-md-1:nth-child(7) .form-control"

    ansibleConfigPreview = ".ansible-wizard-config-preview"
    DeploymentMsg = "div:nth-child(1) > span:nth-child(2)"
    DeploymentMsgText = "Generated Ansible inventory : /etc/ansible/hc_wizard_inventory.yml"

    FinishButton = ".wizard-pf-finish"

    spinner = ".spinner"

    DeploymentMsgFail = "div:nth-child(1) > span:nth-child(2)"
    DeploymentMsgFailText = "Deployment failed"

    def time_sleep(self, sleepTime):
        time.sleep(sleepTime)

    def setup(self):
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = self.ACCEPT_UNTRUSTED_CERTS
        driver = webdriver.Firefox(firefox_profile=profile)
        return driver

    def open_page(self, driver):
        driver.get(self.URL)

    def login(self, driver):
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.loginUserInput)))
        loginUserInput = driver.find_element_by_id(self.loginUserInput)
        loginUserInput.send_keys(self.loginUserInputValue)
        loginPasswordInput = driver.find_element_by_id(self.loginPasswordInput)
        loginPasswordInput.send_keys(self.loginPasswordInputValue)
        loginButton = driver.find_element_by_id(self.loginButton)
        loginButton.click()

    def switchFrame(self, driver, frameRef):
        driver.switch_to_frame(frameRef)

    def assertHostedEngine(self, driver):
        HostedEngine = driver.find_element_by_link_text(self.hostedEngineButtonText)
        assert HostedEngine.text == self.hostedEngineButtonText
        HostedEngine.click()

    def startGlusterDeployment(self, driver):
        GlusterWizard = driver.find_element_by_xpath(self.glusterWizardButton)
        assert GlusterWizard.text == self.glusterWizardButtonText
        GlusterWizard.click()

    def startThreeNodeWizard(self, driver):
        ThreeNodeDep = driver.find_element_by_css_selector(self.ThreeNodeDepButton)
        assert ThreeNodeDep.text == self.ThreeNodeDepButtonText
        ThreeNodeDep.click()

    def sendHostValuesForThreeNodeDep(self, driver, h1, h2, h3):
        driver.find_element_by_css_selector(self.host1Input).send_keys(h1)
        driver.find_element_by_css_selector(self.host2Input).send_keys(h2)
        driver.find_element_by_css_selector(self.host3Input).send_keys(h3)

    def wizardNextClick(self, driver):
        driver.find_element_by_css_selector(self.wizardNextButton).click()

    def fqdnAssertCheck(self, driver):
        fqdnAssert = driver.find_element_by_css_selector(self.fqdnAssertBox)
        assert fqdnAssert.text == self.fqdnAssertBoxValue

    def packageAssertCheck(self, driver):
        packageAssert = driver.find_element_by_css_selector(self.packageAssertBox)
        assert packageAssert.text == self.packageAssertBoxValue

    def volumeAssertCheck(self, driver, click):
        AddVolume = driver.find_element_by_css_selector(self.addVolumeButton)
        assert AddVolume.text == self.addVolumeButtonValue
        if(click):
            AddVolume.click()

    def volumeAddCheck(self, driver, volName):
        EmptyVolumeName = driver.find_element_by_css_selector(self.EmptyVolumeName)
        assert EmptyVolumeName.text == self.EmptyVolumeNameText
        EmptyVolumeName.send_keys(volName)

    def raidAssertCheck(self, driver):
        RaidInformationTitle = driver.find_element_by_css_selector(self.RaidInformationTitle)
        assert RaidInformationTitle.text == self.RaidInformationTitleText

    def raidTypeChange(self, driver, raidType):
        RaidTypeDropDown = driver.find_element_by_css_selector(self.RaidTypeDropDown)
        assert RaidTypeDropDown.text == self.RaidTypeDropDownText
        RaidTypeDropDown.click()
        driver.find_element_by_link_text(raidType).click()
        assert RaidTypeDropDown.text == raidType

    def assertPreview(self, driver):
        ansibleConfig = driver.find_element_by_css_selector(self.ansibleConfigPreview)
        print ansibleConfig.text
        DeploymentMsg = driver.find_element_by_css_selector(self.DeploymentMsg)
        assert DeploymentMsg.text == self.DeploymentMsgText

    def deployGluster(self, driver):
        driver.find_element_by_css_selector(self.FinishButton).click()

    def spinnerCheck(self, driver):
        spinner = driver.find_element_by_css_selector(self.spinner)
        try:
            while spinner.is_displayed():
                print "check: "
        except:
            print "Element not visible"

    def deploymentFailCheck(self, driver):
        DeploymentMsg = driver.find_element_by_css_selector(self.DeploymentMsgFail)
        assert DeploymentMsg.text == self.DeploymentMsgFailText

    def emptyHostAssertCheck(self, driver):
        host1 = driver.find_element_by_css_selector(self.host1Error)
        host2 = driver.find_element_by_css_selector(self.host2Error)
        host3 = driver.find_element_by_css_selector(self.host3Error)

        assert host1.text == self.hostEmptyErrorValue
        assert host2.text == self.hostEmptyErrorValue
        assert host3.text == self.hostEmptyErrorValue

    def handleSameFqdnAsHostCheck(self, driver):
        handleSameFqdnAsHostButton = driver.find_element_by_id(self.handleSameFqdnAsHost)
        handleSameFqdnAsHostButton.click()

    def fqdnUnreachableErrorCheck(self, driver):
        fqdn1_Error = driver.find_element_by_css_selector(self.fqdn1Error)
        fqdn2_Error = driver.find_element_by_css_selector(self.fqdn2Error)

        assert fqdn1_Error.text == self.fqdnUnreachableError
        assert fqdn2_Error.text == self.fqdnUnreachableError

    def fqdnInput(self, driver, fqdn1, fqdn2):
        fqdn1_textArea = driver.find_element_by_id(self.fqdn1Input)
        fqdn1_textArea.send_keys(fqdn1)
        fqdn2_textArea = driver.find_element_by_css_selector(self.fqdn2Input)
        fqdn2_textArea.send_keys(fqdn2)

    def fqdnSameError(self, driver):
        fqdnSameError = driver.find_element_by_css_selector(self.fqdnError)
        assert fqdnSameError.text == self.fqdnSameErrorValue

    def fqdn2Clear(self, driver):
        fqdn2_textArea = driver.find_element_by_css_selector(self.fqdn2Input)
        fqdn2_textArea.clear()

    def fqdnEmptyError(self, driver):
        fqdnEmptyError = driver.find_element_by_css_selector(self.fqdnError)
        assert fqdnEmptyError.text == self.fqdnEmptyError

    def emptyVolumeCheck(self, driver):
        assert driver.find_element_by_css_selector(self.ErrorVolumeName).text == self.ErrorVolumeNameValue
        assert driver.find_element_by_css_selector(self.ErrorGlusterBrickDirectory).text == self.ErrorGlusterBrickDirectory

    def deleteVolumeRow(self, driver, deleteVolume):
        driver.find_element_by_css_selector(deleteVolume).click()

    def vdoCheck(self, driver):
        try:
            vdocheck = driver.find_element_by_css_selector(self.vdoCheckBox)
            vdocheck.click()

            h1Size = driver.find_element_by_css_selector(self.h1Size)
            h1VdoSize = driver.find_element_by_css_selector(self.h1VdoSize)
            assert 10*int(h1Size.get_attribute('value')) == int(h1VdoSize.get_attribute('value'))

            h2Size = driver.find_element_by_css_selector(self.h2Size)
            h2VdoSize = driver.find_element_by_css_selector(self.h2VdoSize)
            assert 10*int(h2Size.get_attribute('value')) == int(h2VdoSize.get_attribute('value'))

            h3Size = driver.find_element_by_css_selector(self.h3Size)
            h3VdoSize = driver.find_element_by_css_selector(self.h3VdoSize)
            assert 10*int(h3Size.get_attribute('value')) == int(h3VdoSize.get_attribute('value'))

        except:
            print "VDO not present"

    def driver_close(self, driver):
        driver.close()
        driver.quit()
