import { createRouter, createWebHashHistory } from 'vue-router'
import { ActiveUser } from "@/services/user";
import { h,resolveComponent } from 'vue';

const MainContainer = () => import("@/containers/MainContainer");
const HomeView = () => import('@/views/HomeView');
const PositionsView = () => import('@/views/PositionsView');
const AboutView = () => import('@/views/AboutView');

const LoginView = () => import('@/views/LoginView');
const Page404 = () => import('@/views/PageNotFound');


const router = createRouter({
  mode: 'history',
  linkActiveClass: 'active',
  scrollBehaviour: () => ({ y: 0 }),
  routes: configRoutes(),
  history: createWebHashHistory(),
});

const isOpenAccess = (route) => route.matched.some((route) => route.meta?.isOpenAccess);

const isFound = (route) => route.matched[0].name !== "NotFound";

router.beforeEach((to, from, next) => {
  if(to.meta?.getTitle) to.meta.title = to.meta.getTitle(to);
  const isAuthenticated = ActiveUser.get();
  if (!isAuthenticated && !isOpenAccess(to)) {
    if (isFound(to)) {
      localStorage.setItem('patToLoadAfterLogin', to.path);
    }
    return next({ name: 'ManagementLogin'});
  }
  return next();
});
export default router

function configRoutes() {
  return [
    {
      path: '/',
      name: 'Home',
      component: MainContainer,
      meta: {
        label: "Home",
      },
      children: [
        {
          path: 'home',
          component: HomeView
        },
        {
          path: 'positions',
          component: PositionsView
        },
        {
          path: 'about',
          component: AboutView
        }
      ]
    },
    {
      path: '/account',
      name: 'account',
      meta: {
        isOpenAccess: true,
      },
      component: {
        render() {
          return h(resolveComponent('router-view'));
        },
      },
      children: [
        {
          path: 'login',
          name: 'Login',
          component: LoginView,
        },
        // {
        //   path: 'forgot',
        //   name: 'Forgot password',
        //   component: ForgotPassword,
        // },
        // {
        //   path: 'reset/:token',
        //   name: 'Password reset',
        //   component: ResetPassword,
        // },
        {
          path: 'login_management',
          name: 'ManagementLogin',
          component: LoginView,
          props: {
            show_email_login: true
          }
        },
      ],
    },
    {
      path: "/:pathMatch(.*)*",
      name: 'NotFound',
      component: Page404,
    }
  ]
}
