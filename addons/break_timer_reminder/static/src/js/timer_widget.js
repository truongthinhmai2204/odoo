/** @odoo-module **/

import { Component, onWillStart, mount, xml } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class TimerWidget extends Component {
    setup() {
        this.timer = null;
        this.remainingSeconds = 1500;
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
                this.notification.add("⏰ Hết giờ! Nghỉ thôi!", { type: "success" });
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

    get formattedTime() {
        return this.formatTime(this.remainingSeconds);
    }
}
TimerWidget.template = xml/* xml */ `
    <div class="o_timer_widget" style="text-align:center; padding:1rem;">
        <h2 t-esc="formattedTime"/>
        <div style="margin-top: 1rem;">
            <button t-on-click="startTimer">▶️ Bắt đầu</button>
            <button t-on-click="stopTimer">⏸️ Dừng</button>
            <button t-on-click="resetTimer">🔄 Reset</button>
        </div>
    </div>
`;

// Gắn widget vào phần tử cụ thể trong DOM khi DOM đã sẵn sàng
document.addEventListener("DOMContentLoaded", () => {
    const target = document.querySelector("my_timer_widget");
    if (target) {
        mount(TimerWidget, { target });
    }
});
