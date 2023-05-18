<template>
    <div class="p-app">
        <div class="p-header">
            <span>header</span>
        </div>
        <div class="p-body">
            <main class="p-main">
                <router-view :key="$route.path"></router-view>
            </main>
        </div>
        <div class="p-footer">
            <span>footer</span>
        </div>
    </div>
</template>
<script>
export default {
    name: 'MainContainer',
}
</script>