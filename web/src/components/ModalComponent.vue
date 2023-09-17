<template>
    <div class="c-modal-wrapper" v-show="show" data-cy="modal">
        <div class="c-modal">
            <div class="c-modal-header">
                <h5>{{ title }}</h5>
                <slot name="header"></slot>
                <button @click="close">
                    X
                </button>
            </div>
            <div class="c-modal-body">
                <slot name="body"></slot>
            </div>
            <div class="c-modal-footer">
                <slot name="footer"></slot>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "ModalComponent",
    props: {
        show: {
            type: Boolean,
            default: false,
        },
        title: String,
    },
    methods: {
        close() {
            this.$emit('close');
        }
    }
}
</script>
<style>
.c-modal-wrapper {
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    height: 100%;
    width: 100%;

}
.c-modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 0.5em;
    padding: 5px;
    border-bottom: 1px solid #F4D03F;
}
.c-modal-footer {
    margin-top: 1em;
    display: flex;
    justify-content: center;
}
.c-modal-body {
    display: flex;
    flex-direction: column;
    margin-top: 1em;
    gap: 1em;
    align-items: center;
}
.c-modal {
    width: 400px;
    height: 200px;
    margin-left: 32%;
    margin-top: 20%;
    padding: 10px 10px;
    background-color: #474747;
    border: 1px solid #F4D03F;
    border-radius: 3%;
}
</style>