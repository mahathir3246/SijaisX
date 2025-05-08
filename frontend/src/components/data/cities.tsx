export const cityOptions = [
    { label: 'Helsinki', value: 'helsinki' },
    { label: 'Espoo',    value: 'espoo'   },
    { label: 'Vantaa',   value: 'vantaa'  }
  ] as const;
  export type CityValue = (typeof cityOptions)[number]['value'];