import selenium
from selenium import webdriver
import shelve
from selenium.webdriver.chrome.options import Options

"""
1、要先获取到企业微信的cookie
    -采用复用已有浏览器的方式（只能使用chrome，window先把chrome快捷方式地址配置到path环境变量，关闭所有chrome浏览器页面，命令行执行chrome --remote-debugging-port=9222）
    -在打开的chrome浏览器中登录企业微信后台管理账号
    -在setup方法中，设置调试器地址 (debugger_address)，设置的端口号与命令行执行的一致，引用option时要注意引用chrome的，代码语句如下：
        option = Options()
        option.debugger_address = "localhost:9222"
    -在实例化driver对象时，注意此处是chrome的，然后参数方法要使用options=，代码语句如下：
        self.driver = webdriver.Chrome(options=option)
2、在test_cookie方法中，要先去获取cookie，使用driver.get_cookies方法，并在控制台输出以便使用，代码语句如下：
    cookies = self.driver.get_cookies()
    print(cookies)
3、然后执行test_cookie方法，获取到cookies，在控制台复制并赋值给自定义变量cookies
4、此时已获取到cookies，则实例化driver时，不再需要复用浏览器cookie，即把实例化中参数删去；并且不需要重复获取和输出cookies，即注释掉2、中的代码
5、使用for循环和driver.add_cookie方法将cookie添加，用以完成登录验证(添加cookie如果遇到浮点型的参数，运行会报错，这种情况，可以去做处理，在for循环中添加if判断，通过对应key值判断，pop删除这个值)
6、然后就可以进行登陆后的操作验证等
"""

class TestSelenium:
    def setup(self):
        # option = Options()
        # option.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    # def test_get_cookie(self):
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    #     # cookies = self.driver.get_cookies()


    def test_add_user(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': True,
                    'value': 'faVYXh45Jk0gtvZtKZXexarNlJYUgIHhM_7jR42qWi8C8bTfjrwZDzfxtUtC0Bbade9Ejeb5_uhlOUZ9Y8HPBXs5Ha106JOctUQQe8UuQJdnk_swO57CURQO_iwBJDqFVcZT27hDOlRQxqk4eNYQygVAnXSn6IPdNQgRVeZAreDKijfoC_Hlgbmxu5n9HzwjJ3E1xT3j4fRkd97gZXZF3OlZq8mRY1rwPgeqoW7WHmunfwtfJlQ2fkoIlHBWd_i1UMqSJmutRz5CdT17jHdk_Q'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': True,
                    'value': 'zC1dChRiUNfvgF4yFEY1n6R__bfY8RHDTlpfpxdCtfbRbg-rLnQpEmPIg69whH4W'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/',
                    'secure': True, 'value': 'a3496896'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                    'secure': True, 'value': '1970325000153152'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/',
                    'secure': True, 'value': '399940969153383'},
                   {'domain': '.work.weixin.qq.com', 'expiry': 1600399143.343489, 'httpOnly': False,
                    'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': True,
                    'value': '5680107520'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'property20', 'path': '/', 'secure': True,
                    'value': '2182F6BFF469B67A754A3B0CEB929451DA4DC2EB18BF2BAE73A896A222368AD1DC23EA029A6E3C87'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
                    'value': '759a3915f4a2271bb0b936f5de3ca07e52d835c85910e6d93a5d92f4f46f42cb'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'rv2', 'path': '/', 'secure': True,
                    'value': '80452537295B5AAC7F8E800103771A866154E84D3DDFCEF148'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'sd_userid', 'path': '/', 'secure': True,
                    'value': '8261585032971231'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': True,
                    'value': '1970712917'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': True, 'value': '0'},
                   {'domain': '.qq.com', 'httpOnly': True, 'name': 'ied_qq', 'path': '/', 'secure': True,
                    'value': 'o1970712917'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'slgqqcomrouteLine', 'path': '/', 'sameSite': 'Lax',
                    'secure': True, 'value': 'index'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
                    'value': 'GlZp4UTDSx'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'uin', 'path': '/', 'secure': True,
                    'value': 'o1970712917'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': True,
                    'value': '2kn99mv'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/',
                    'secure': True, 'value': '1'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'dnfqqcomrouteLine', 'path': '/', 'sameSite': 'Lax',
                    'secure': True,
                    'value': 'index_main_a20200423version_a20200423version_a20200319challenge_a20200319arad2_a20121026gbook'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'tokenParams', 'path': '/', 'sameSite': 'Lax',
                    'secure': True, 'value': '%3Fe_code'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': True,
                    'value': '5016462912'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True,
                    'value': 'direct'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'eas_sid', 'path': '/', 'secure': True,
                    'value': 'R105p8x7D680E2N0R2t4T672O1'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_si', 'path': '/', 'secure': True,
                    'value': 's9483341824'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/',
                    'secure': True, 'value': '1688850346057263'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'skey', 'path': '/', 'secure': True,
                    'value': '@teJJ7b6tl'},
                   {'domain': 'work.weixin.qq.com', 'expiry': 1597833952.401576, 'httpOnly': True, 'name': 'ww_rtkey',
                    'path': '/', 'secure': False, 'value': '2kn99mv'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': True,
                    'value': 'ssid=s5589898944&pgvReferrer='},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/',
                    'secure': True, 'value': '1688850346057263'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/',
                    'secure': True, 'value': '0'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': True,
                    'value': '1_1970712917'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'sd_cookie_crttime', 'path': '/', 'secure': True,
                    'value': '1585032971231'}]

        db = shelve.open("db/logincookies")
        db['cookie'] = cookies
        db.close()
        # cookies = self.driver.get_cookies()
        # print(cookies)
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        self.driver.find_element_by_css_selector('[id=js_upload_file_input]').send_keys("D:\wy\\123test.xlsx")
        file_name = self.driver.find_element_by_css_selector('#upload_file_name').text
        assert "123test.xlsx" == file_name
