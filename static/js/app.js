$(document).ready(function () {
    const templates = {
      mirai: {
        qq: "请填写机器人的 QQ 号",
        manager_qq: "请修改为机器人管理员的QQ号（你自己的 QQ 号）",
        api_key: "__QUOTE__1234567890__QUOTE__",
        reverse_ws_host: "__QUOTE__0.0.0.0__QUOTE__",
        reverse_ws_port: 8554,
      },
      onebot: {
        qq: "请修改为你机器人的QQ号",
        manager_qq: "请修改为机器人管理员的QQ号",
        reverse_ws_host: "__QUOTE__0.0.0.0__QUOTE__",
        reverse_ws_port: 8566,
      },
      telegram: {
        bot_token: "__QUOTE__你的 Bot token__QUOTE__",
        proxy: "__QUOTE__http://localhost:1080__QUOTE__",
        manager_chat: 1234567890,
      },
      discord: {
        bot_token: "__QUOTE__xxx__QUOTE__",
      },
      openai: {
        browserless_endpoint: "__QUOTE__https://chatgpt-proxy.lss233.com/api/__QUOTE__",
        api_endpoint: "__QUOTE__https://api.openai.com/v1__QUOTE__",
        accounts: {
          access_token: "__QUOTE__一串 ey 开头的东西__QUOTE__",
          api_key: "__QUOTE__sk-xxxx__QUOTE__",
        },
      },
      bing: {
        wss_link: "__QUOTE__wss://sydney.bing.com/sydney/ChatHub__QUOTE__",
        bing_endpoint: "__QUOTE__https://edgeservices.bing.com/edgesvc/turing/conversation/create__QUOTE__",
        accounts: {
          cookie_content: '__QUOTE__你的结果__QUOTE__',
        },
      },
      bard: {
        accounts: {
          cookie_content: '__QUOTE__xxx__QUOTE__',
        },
      },
      yiyan: {
        accounts: {
          cookie_content: '__QUOTE__BDUSS=xxxxxxxxx__QUOTE__',
        },
      },
      chatglm: {
        accounts: {
          api_endpoint: "__QUOTE__http://127.0.0.1:8000__QUOTE__",
          max_turns: 10,
          timeout: 360,
        },
      },
      poe: {
        accounts: {
          p_b: "__QUOTE__V4j***__QUOTE__",
        },
      },
      text_to_speech: {
        always: false,
        default: "__QUOTE__zh-CN-XiaoyouNeural__QUOTE__",
        engine: "__QUOTE__edge__QUOTE__",
      },
      text_to_image: {
        always: true,
        font_size: 30,
        width: 700,
        font_path: "__QUOTE__fonts/sarasa-mono-sc-regular.ttf__QUOTE__",
        offset_x: 50,
        offset_y: 50,
      },
      // ... 其他节点
    };
    const optionsMap = {
        "accounts": ["mirai", "telegram", "discord", "onebot"],
        "ai-platforms": ["openai", "bing", "bard", "yiyan", "chatglm", "poe"],
        "misc-settings": ["text_to_speech", "text_to_image"]
    };


    // 修改此行以分别处理选项
    $('button[data-toggle="modal"]').on('click', function () {
        const buttonId = $(this).attr('id');
        const targetElementId = buttonId.substring(4); // 删除前缀
        console.log('Button ID:', buttonId); // 输出调试信息
        console.log('Target Element ID:', targetElementId); // 输出调试信息
        $('#' + targetElementId).data('blockTarget', targetElementId);
        
        //展示按钮
        const optionsToShow = optionsMap[targetElementId];
        $('.option-container').hide();
        optionsToShow.forEach(option => {
            $(`#${option}`).show();
        });
    });

    
    // 添加事件监听器
    const accountsConfirm = document.getElementById("accounts-confirm");
    const aiPlatformsConfirm = document.getElementById("ai-platforms-confirm");
    const miscSettingsConfirm = document.getElementById("misc-settings-confirm");
    
    accountsConfirm.addEventListener("click", function () {
        handleOptionSelection('accounts-block');
    });
    
    aiPlatformsConfirm.addEventListener("click", function () {
        handleOptionSelection('ai-platforms-block');
    });
    
    miscSettingsConfirm.addEventListener("click", function () {
        handleOptionSelection('misc-settings-block');
    });
    
    // 添加配置项
    function handleOptionSelection(targetElementId) {
    const selectedOption = $(`input[name="${targetElementId}-option"]:checked`).val();
        console.log('Selected Option:', selectedOption); // 输出调试信息
        const targetElement = $(`#${targetElementId}`);
        addConfigItems(targetElement, templates[selectedOption]);
        $(`input[name="${targetElementId}-option"]`).prop('checked', false);
    
        // 关闭对应的模态框
        let modalId = "";
        switch (targetElementId) {
            case "accounts-block":
                modalId = "accountsModal";
                break;
            case "ai-platforms-block":
                modalId = "aiPlatformsModal";
                break;
            case "misc-settings-block":
                modalId = "miscSettingsModal";
                break;
            default:
                break;
        }
        console.log('Modal ID:', modalId); // 输出调试信息
        $('#' + modalId).modal('hide');
    }


    function addConfigItems(container, template) {
        for (const key in template) {
            const value = template[key];
            const labelText = $("<div>").addClass("label-text").text(key);
            container.append(labelText);
            if (typeof value === "object") {
                addConfigItems(container, value);
            } else {
                const input = $("<input>").addClass("config-input").val(value);
                container.append(input);
            }
            container.append($("<br>"));
        }
    }

    $("#save_button").click(function () {
        const data = {}; // 创建一个空对象用于保存数据
        $(".block").each(function () {
            const blockData = {};
            const blockId = $(this).attr("id");

            if (blockId === 'ai-platforms-block') {
                const template = $(this).find('.template').val();
                data[template] = blockData;
                data[template + ".accounts"] = {};
            } else {
                data[blockId] = blockData;
            }

            $(this).find(".config-input").each(function () {
                const key = $(this).siblings(".label-text").text();
                const value = $(this).val();
                if (blockId === 'ai-platforms-block') {
                    data[template + ".accounts"][key] = value;
                } else {
                    blockData[key] = value;
                }
            });
        });

        $.ajax({
            url: "/save",
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify(data),
            success: function (response) {
                const file_id = response.file_id;
                const download_url = "/download/" + file_id;
                const link = $("<a>").attr("href", download_url).text("Download config");
            $("#download_link").html(link);
        },
        error: function () {
            alert("Error occurred while saving the configuration. Please try again.");}
        });
})
});