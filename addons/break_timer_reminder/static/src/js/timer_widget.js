/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class TimerWidget extends Component {
    setup() {
        this.state = useState({ remainingSeconds: 1500, timer: null });
        this.notification = useService("notification");
    }

    formatTime(seconds) {
        const min = String(Math.floor(seconds / 60)).padStart(2, '0');
        const sec = String(seconds % 60).padStart(2, '0');
        return `${min}:${sec}`;
    }

    startTimer() {
        if (this.state.timer) return;
        this.state.timer = setInterval(() => {
            if (this.state.remainingSeconds > 0) {
                this.state.remainingSeconds--;
            } else {
                clearInterval(this.state.timer);
                this.state.timer = null;
                this.notification.add("Hết giờ! Nghỉ thôi nào!", { type: "success" });
            }
        }, 1000);
    }

    stopTimer() {
        clearInterval(this.state.timer);
        this.state.timer = null;
    }

    resetTimer() {
        this.stopTimer();
        this.state.remainingSeconds = 1500;
    }
}

TimerWidget.template = "break_timer_reminder.timer_widget";
registry.category("actions").add("break_timer_reminder.timer_widget", TimerWidget);
