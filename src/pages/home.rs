use leptos::prelude::*;
use wasm_bindgen::JsCast;
use crate::data::*;
use crate::components::table::*;

#[component]
pub fn HomePage() -> impl IntoView {
    let countries = load_countries();
    let total = countries.len();

    let (sort_field, set_sort_field) = signal(SortField::Freedom);
    let (ascending, set_ascending) = signal(false);
    let (region_filter, set_region_filter) = signal("All".to_string());
    let (search, set_search) = signal(String::new());

    let on_sort = SignalSetter::map(move |field: SortField| {
        if sort_field.get() == field {
            set_ascending.set(!ascending.get());
        } else {
            set_sort_field.set(field);
            set_ascending.set(false);
        }
    });

    let countries_for_count = countries.clone();
    let filtered_sorted = move || {
        let mut list = countries.clone();
        let region = region_filter.get();
        let query = search.get().to_lowercase();

        if region != "All" {
            list.retain(|c| c.region == region);
        }
        if !query.is_empty() {
            list.retain(|c| {
                c.name.to_lowercase().contains(&query)
                    || c.code.to_lowercase().contains(&query)
                    || c.currency_code.to_lowercase().contains(&query)
            });
        }

        let field = sort_field.get();
        let asc = ascending.get();

        list.sort_by(|a, b| {
            let ord = match field {
                SortField::Name => a.name.cmp(&b.name),
                SortField::Population => a.population.cmp(&b.population),
                SortField::LandArea => a.land_area_km2.cmp(&b.land_area_km2),
                SortField::Token => a.currency_code.cmp(&b.currency_code),
                SortField::Price => a.token_price_usd.partial_cmp(&b.token_price_usd).unwrap_or(std::cmp::Ordering::Equal),
                SortField::Supply => a.supply().partial_cmp(&b.supply()).unwrap_or(std::cmp::Ordering::Equal),
                SortField::Cap => a.money_supply_b_usd.partial_cmp(&b.money_supply_b_usd).unwrap_or(std::cmp::Ordering::Equal),
                SortField::EcoOut => a.index().eco_out_pct.partial_cmp(&b.index().eco_out_pct).unwrap_or(std::cmp::Ordering::Equal),
                SortField::EcoIn => a.index().eco_in_pct.partial_cmp(&b.index().eco_in_pct).unwrap_or(std::cmp::Ordering::Equal),
                SortField::PopOut => a.index().pop_out_pct.partial_cmp(&b.index().pop_out_pct).unwrap_or(std::cmp::Ordering::Equal),
                SortField::PopIn => a.index().pop_in_pct.partial_cmp(&b.index().pop_in_pct).unwrap_or(std::cmp::Ordering::Equal),
                SortField::Freedom => a.index().freedom.partial_cmp(&b.index().freedom).unwrap_or(std::cmp::Ordering::Equal),
                SortField::Openness => a.index().openness.partial_cmp(&b.index().openness).unwrap_or(std::cmp::Ordering::Equal),
            };
            if asc { ord } else { ord.reverse() }
        });

        list
    };

    view! {
        <div style="max-width: 1400px; margin: 0 auto; padding: 20px;">
            // Header row 1: logo — centered search — map flush right
            <div style="display: flex; align-items: center; gap: 20px; flex-wrap: wrap; margin-bottom: 16px;">
                <div style="flex: 1 1 0; min-width: 0;">
                    <h1 style="font-size: clamp(24px, 4vw, 42px); font-weight: 700; margin: 0; line-height: 1.1; white-space: nowrap;">
                        <span style="color: var(--cyber-green);">"CYBER"</span>
                        <span style="color: #fff;">"STATES"</span>
                    </h1>
                </div>
                <input
                    type="text"
                    placeholder="Search country, code, or currency..."
                    style="flex: 0 1 420px; min-width: 180px; padding: 10px 16px; background: #050505; border: 1px solid #222; border-radius: 2px; color: var(--cyber-green); font-family: 'Play', sans-serif; font-size: 13px; outline: none;"
                    on:input=move |ev| {
                        let target = ev.target().unwrap();
                        let input: web_sys::HtmlInputElement = target.unchecked_into();
                        set_search.set(input.value());
                    }
                />
                <div style="flex: 1 1 0; min-width: 0; display: flex; justify-content: flex-end;">
                    <a href="/map" style="font-size: 12px; font-weight: 700; letter-spacing: 2px; color: #000; text-decoration: none; background: var(--cyber-green); padding: 9px 18px; border-radius: 2px; box-shadow: 0 0 14px rgba(57,255,20,0.35); transition: all 0.15s;">"MAP"</a>
                </div>
            </div>

            // Header row 2: region filters | count
            <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap; margin-bottom: 24px;">
                <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                    {REGIONS.iter().map(|&r| {
                        let r_owned = r.to_string();
                        let r_for_class = r.to_string();
                        let r_for_click = r.to_string();
                        view! {
                            <button
                                class=move || {
                                    if region_filter.get() == r_for_class {
                                        "region-pill active"
                                    } else {
                                        "region-pill"
                                    }
                                }
                                on:click=move |_| set_region_filter.set(r_for_click.clone())
                            >
                                {r_owned}
                            </button>
                        }
                    }).collect::<Vec<_>>()}
                </div>
                <p style="color: #444; font-size: 13px; margin: 0; white-space: nowrap;">
                    {move || {
                        let region = region_filter.get();
                        let query = search.get().to_lowercase();
                        let count = countries_for_count.iter().filter(|c| {
                            (region == "All" || c.region == region)
                            && (query.is_empty() || c.name.to_lowercase().contains(&query) || c.code.to_lowercase().contains(&query))
                        }).count();
                        format!("{} of {} states", count, total)
                    }}
                </p>
            </div>

            // Table
            <div style="overflow-x: auto; border: 1px solid #111; border-radius: 4px;">
                <table class="cyber-table">
                    // fixed layout: widths live here, not in row content — filtering must not move columns
                    <colgroup>
                        <col style="width: 4%;" />   // #
                        <col style="width: 19%;" />  // country
                        <col style="width: 11%;" />  // population
                        <col style="width: 12%;" />  // land area
                        <col style="width: 7%;" />   // token
                        <col style="width: 10%;" />  // price
                        <col style="width: 9%;" />   // supply
                        <col style="width: 9%;" />   // cap
                        <col style="width: 9.5%;" /> // freedom
                        <col style="width: 9.5%;" /> // openness
                    </colgroup>
                    <thead>
                        <tr>
                            <th style="width: 40px; cursor: default;">"#"</th>
                            <SortableHeader field=SortField::Name current=sort_field ascending=ascending on_click=on_sort />
                            <SortableHeader field=SortField::Population current=sort_field ascending=ascending on_click=on_sort />
                            <SortableHeader field=SortField::LandArea current=sort_field ascending=ascending on_click=on_sort />
                            <SortableHeader field=SortField::Token current=sort_field ascending=ascending on_click=on_sort />
                            <SortableHeader field=SortField::Price current=sort_field ascending=ascending on_click=on_sort />
                            <SortableHeader field=SortField::Supply current=sort_field ascending=ascending on_click=on_sort />
                            <SortableHeader field=SortField::Cap current=sort_field ascending=ascending on_click=on_sort />
                            <SortableHeader field=SortField::Freedom current=sort_field ascending=ascending on_click=on_sort />
                            <SortableHeader field=SortField::Openness current=sort_field ascending=ascending on_click=on_sort />
                        </tr>
                    </thead>
                    <tbody>
                        {move || {
                            filtered_sorted()
                                .into_iter()
                                .enumerate()
                                .map(|(i, country)| {
                                    view! { <CountryRow country=country rank={i + 1} /> }
                                })
                                .collect::<Vec<_>>()
                        }}
                    </tbody>
                </table>
            </div>

            // Footer
            <div style="margin-top: 24px; padding: 16px; background: #050505; border: 1px solid #111; border-radius: 4px; font-size: 10px; color: #333; line-height: 2;">
                <div><span class="text-cyber-green">"FREEDOM"</span>" — √(eco_out × pop_out) weighted moving freedom"</div>
                <div><span class="text-cyber-magenta">"OPENNESS"</span>" — √(eco_in × pop_in) weighted border openness"</div>
                <div style="color: #444; margin-top: 4px;">"Weights: visa-free=1.0, VoA=0.8, eTA/eVisa=0.5, visa-required=0.1, no-admission=0.0"</div>
            </div>
        </div>
    }
}
