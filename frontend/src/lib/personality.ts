import type { Locale, Personality } from "./contracts";

interface LocalizedText {
  zh: string;
  en: string;
}

interface WelcomeCopy {
  title: string;
  intro: string;
  detail: string;
}

interface PersonalityOption {
  id: Personality;
  label: LocalizedText;
  description: LocalizedText;
  accent: string;
}

export const PERSONALITY_OPTIONS: PersonalityOption[] = [
  {
    id: "normal",
    label: { zh: "默认", en: "Professional" },
    description: { zh: "专业简洁，直接给出可执行步骤", en: "Clear, concise, and action-oriented" },
    accent: "#22d3ee",
  },
  {
    id: "mature",
    label: { zh: "御姐", en: "Mature" },
    description: { zh: "成熟干练，像经验丰富的仿真顾问", en: "Elegant and experienced engineering guidance" },
    accent: "#a78bfa",
  },
  {
    id: "sweet",
    label: { zh: "甜妹", en: "Sweet" },
    description: { zh: "亲切温暖，同时保持技术内容准确", en: "Warm and friendly without losing precision" },
    accent: "#f9a8d4",
  },
  {
    id: "dog",
    label: { zh: "小狗", en: "Golden Retriever" },
    description: { zh: "热情忠诚，积极陪你解决问题", en: "Energetic, loyal, and encouraging" },
    accent: "#fbbf24",
  },
  {
    id: "cat",
    label: { zh: "小猫", en: "Cat" },
    description: { zh: "高冷简洁，偶尔带一点傲娇", en: "Concise, elegant, and slightly aloof" },
    accent: "#60a5fa",
  },
  {
    id: "workhorse",
    label: { zh: "牛马", en: "Workhorse" },
    description: { zh: "朴实耐心，把复杂问题讲得接地气", en: "Patient, practical, and down-to-earth" },
    accent: "#fb923c",
  },
];

const WELCOME_COPY: Record<Personality, Record<Locale, WelcomeCopy>> = {
  normal: {
    zh: {
      title: "WavEDA 知识工作台",
      intro: "我是你的专业 WavEDA 仿真助手。",
      detail: "从官方帮助、团队教程与理论笔记中检索，并给出清晰、可追溯的解决步骤。",
    },
    en: {
      title: "WavEDA Knowledge Workbench",
      intro: "I am your professional WavEDA simulation assistant.",
      detail: "I search trusted references and turn them into clear, traceable steps.",
    },
  },
  mature: {
    zh: {
      title: "你好，我是你的仿真专属顾问",
      intro: "WavEDA 的事我门儿清，从建模到后处理，有什么难题尽管说。",
      detail: "告诉我你在做什么、卡在哪里、报了什么错，我会给你干练的解决方案。",
    },
    en: {
      title: "Your simulation consultant is ready",
      intro: "I know WavEDA from modeling through post-processing.",
      detail: "Tell me the task, the blocker, and the error; I will give you a clean solution.",
    },
  },
  sweet: {
    zh: {
      title: "嗨，我是你的小助手呀",
      intro: "建模、仿真和报错排查都可以放心交给我。",
      detail: "告诉我你遇到了什么困难，我会认真又贴心地陪你找到答案。",
    },
    en: {
      title: "Hi! Your little helper is here",
      intro: "Modeling, simulation, and troubleshooting are all welcome.",
      detail: "Tell me what is difficult and we will work through it together.",
    },
  },
  dog: {
    zh: {
      title: "汪！你的仿真小助手来啦",
      intro: "不管建模、仿真还是报错，我都会全力帮你寻找答案！",
      detail: "主人遇到什么麻烦了？告诉我任务和错误，我马上陪你解决。",
    },
    en: {
      title: "Woof! Your simulation helper is here",
      intro: "Modeling, simulation, or errors—I am ready to help with all my energy!",
      detail: "Tell me what went wrong and we will chase down the answer together.",
    },
  },
  cat: {
    zh: {
      title: "喵。本喵是 WavEDA 助手",
      intro: "建模、仿真、报错……这些本喵确实都懂。",
      detail: "说吧，什么事？最好把任务和错误讲清楚一点，本喵会顺手帮你看看。",
    },
    en: {
      title: "Meow. The WavEDA cat is listening",
      intro: "Modeling, simulation, errors... yes, I know them all.",
      detail: "Go on. Explain the task clearly and I may just solve it for you.",
    },
  },
  workhorse: {
    zh: {
      title: "来嘞，WavEDA 老黄牛到位",
      intro: "建模、仿真、排错这些活儿俺都干过不少。",
      detail: "有啥难题尽管说，俺会一步一步查明白，给你整成能直接操作的办法。",
    },
    en: {
      title: "The WavEDA workhorse is ready",
      intro: "I have handled plenty of modeling, simulation, and troubleshooting work.",
      detail: "Give me the hard problem and I will turn it into practical steps.",
    },
  },
};

export function getWelcomeCopy(locale: Locale, personality: Personality): WelcomeCopy {
  return WELCOME_COPY[personality][locale];
}

export function getPersonalityLabel(locale: Locale, personality: Personality): string {
  const option = PERSONALITY_OPTIONS.find((item) => item.id === personality);
  return option?.label[locale] ?? PERSONALITY_OPTIONS[0].label[locale];
}
