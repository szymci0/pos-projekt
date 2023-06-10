<template>
    <div class="d-flex justify-content-center align-items-cente">
        <v-client-table :data="data.tableData" :columns="data.columns">

        </v-client-table>
    </div>
</template>
<script>
export default {
    name: "UsersView",
    mounted() {

    },
    data() {
        return {
            data: {
                columns: ['id', 'name', 'age'],
                tableData: [
                    { id: 1, name: "John", age: "20" },
                    { id: 2, name: "Jane", age: "24" },
                    { id: 3, name: "Susan", age: "16" },
                    { id: 4, name: "Chris", age: "55" },
                    { id: 5, name: "Dan", age: "40" }
                ],
                options: {
                    // see the options API
                }
            }
        }
    }
}
</script>