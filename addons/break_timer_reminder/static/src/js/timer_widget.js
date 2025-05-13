/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class TimerWidget extends Component {
    setup() {
        this.timer = null;
        this.remainingSeconds = 1500; // 25 phút mặc định
        this.notification = useService("notification");
    }

    formatTime(seconds) {
        const min = String(Math.floor(seconds / 60)).padStart(2, '0');
        const sec = String(seconds % 60).padStart(2, '0');
        return `${min}:${sec}`;
    }

    startTimer() {
        if (this.timer) return;
        this.timer = setInterval(() => {
            if (this.remainingSeconds > 0) {
                this.remainingSeconds--;
                this.render();
            } else {
                clearInterval(this.timer);
                this.timer = null;
                this.notification.add("Hết giờ! Nghỉ thôi nào!", { type: "success" });
            }
        }, 1000);
    }

    stopTimer() {
        clearInterval(this.timer);
        this.timer = null;
    }

    resetTimer() {
        this.stopTimer();
        this.remainingSeconds = 1500;
        this.render();
    }
}

TimerWidget.template = "break_timer_reminder.timer_widget";

registry.category("actions").add("break_timer_reminder.timer_widget.xml", TimerWidget);
