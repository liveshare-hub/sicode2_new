import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path:'/',
        name:'workers.index',
        component: () => import("../views/workers/index.vue")
    },
    {
        path:'/create',
        name:'workers.create',
        component: () => import("../views/workers/create.vue")
    },
    {
        path:'/edit/:id',
        name:'workers.edit',
        component: () => import("../views/workers/edit.vue")
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;