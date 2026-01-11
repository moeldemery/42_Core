/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_sort_algo.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/10 23:34:43 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/10 23:34:45 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int ft_is_sorted(t_list *stack)
{
    t_list *current;

    current = stack;
    while (current && current->next)
    {
        if (*(int *)current->content > *(int *)current->next->content)
            return (0);
        current = current->next;
    }
    return (1);
}

void ft_sort_three(t_list **stack)
{
    int first;
    int second;
    int third;

    if (ft_lstsize(*stack) != 3)
        return ;
    first = *(int *)(*stack)->content;
    second = *(int *)(*stack)->next->content;
    third = *(int *)(*stack)->next->next->content;

    if (first > second && second < third && first < third)
        ft_sa(stack); // sa
    else if (first > second && second > third)
    {
        ft_sa(stack); // sa
        ft_rra(stack);  // rra
    }
    else if (first > second && second < third && first > third)
        ft_rra(stack);  // rra
    else if (first < second && second > third && first < third)
    {
        ft_sa(stack); // sa
        ft_ra(stack);  // ra
    }
    else if (first < second && second > third && first > third)
        ft_ra(stack);  // ra
}
